import os
import queue
import logging

from abc import ABC
from typing import List
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

from sqlalchemy.dialects.mysql import insert as mysql_insert
from sqlalchemy.dialects.sqlite import insert as sqlite_insert

from gemmi import cif

from mmcif_db_utils.schemas import Status, ExperimentTypes
from mmcif_db_utils.models import get_table, cast_type, metadata_obj

logger = logging.getLogger(__name__)


class ModelFileReader:
    """
    A class for reading model files and extracting data from them.

    Args:
        config (dict): Configuration settings for the reader.
        categories (list): List of categories to extract from the model file.
    """

    def __init__(self, config, categories):
        self.config = config
        self.categories = categories
    
    def _table_to_dict(self, category, table):
        """
        Converts a table to a dictionary.

        Args:
            category (str): The category of the table.
            table (Table): The table to convert.

        Returns:
            list: A list of dictionaries representing the rows of the table.

        """
        sql_table = get_table(category)
        if sql_table is None:
            logger.error(f"Model not found for {category}")
            return

        items = [t.split(".")[1] for t in table.tags]
        rows = []

        for r in table:
            row = {}
            for c in sql_table.c:
                if c.name not in items:
                    row[c.name] = None
                    continue

                row[c.name] = cast_type(sql_table, c.name, cif.as_string(r[c.name]))
            rows.append(row)

        return rows

    def read(self, file_path):
        """
        Reads the model file and extracts data.

        Args:
            file_path (str): The path to the model file.

        Returns:
            dict: A dictionary containing the extracted data, with category names as keys.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If no data block is found in the file.

        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        logger.debug(f"Reading file: {file_path}")

        model_data = {}
        doc = cif.read(file_path)
        block = doc[-1]

        if not block:
            raise ValueError(f"No data block found in the file: {file_path}")

        self._entry_id = block.name
        for cat in self.categories:
            table = block.find_mmcif_category(f"_{cat}")

            if not table:
                logger.debug(f"Category {cat} not found in {file_path}")
                continue
        
            model_data[cat] = self._table_to_dict(cat, table)

        return model_data


class DataLoader(ABC):
    """
    A class for loading data into a database using multiple threads.

    Attributes:
        config (Config): The configuration object.
        engine (Engine): The database engine object.
        categories (List[str]): The list of categories to load.
        filelist (List[str]): The list of files to load.
    """

    def __init__(self, config, engine, categories, filelist):
        self.config = config
        self.engine = engine
        self.categories = categories
        self.filelist = filelist

    def _read_data(self, file):
        reader = ModelFileReader(config=self.config, categories=self.categories)

        try:
            return reader.read(file)
        except Exception as e:
            logger.error(f"Error reading file {file}: {e}")
            return {}

    def _engine_load(self, batch_data):
        raise NotImplementedError

    def _data_builder_task(self, worker, file_queue):
        logger.debug(f"Worker {worker} started")
        db_batch = []

        while True:
            try:
                file = file_queue.get()
                file_queue.task_done()
            except file_queue.Empty:
                break

            if file is None:
                break

            data = self._read_data(file)
            if data:
                db_batch.append(data)

            if len(db_batch) >= self.config.batch_size:
                try:
                    self._engine_load(db_batch)
                except Exception as e:
                    logger.error(f"Error loading data for worker {worker} from {file}: {str(e)}")
                finally:
                    db_batch.clear()

        if db_batch:
            logger.info(f"Loading remaining data for worker {worker}")

            try:
                self._engine_load(db_batch)
            except Exception as e:
                logger.error(f"Error loading remaining data for worker {worker}: {str(e)}")
            finally:
                db_batch.clear()

    def load(self):
        """
        Loads the files in the filelist into the database using multiple threads.

        This method uses a thread pool executor to concurrently process the files in the filelist.
        Each file is added to a file queue, which is consumed by worker threads.
        Once all files have been processed, the method waits for all worker threads to complete.

        Returns:
            None

        Raises:
            Any exceptions raised by the worker threads.
        """
        file_queue = queue.Queue(maxsize=self.config.queue_size)

        count = 0
        with ThreadPoolExecutor(max_workers=self.config.num_threads) as executor:
            futures = [executor.submit(self._data_builder_task, worker, file_queue) for worker in range(self.config.num_threads)]

            for file in self.filelist:
                count += 1
                file_queue.put(file)

            file_queue.join()

            # stop signal for the workers
            for _ in range(self.config.num_threads):
                file_queue.put(None)

            for f in as_completed(futures):
                f.result()

        logger.info(f"Loaded {count} files into the database")


class MysqlDataLoader(DataLoader):
    """
    A data loader class for loading data into a MySQL database.

    This class extends the base DataLoader class and provides functionality
    to load data into a MySQL database using upsert (insert or replace) operation.

    Note: The upsert operation is achieved by using `on_duplicate_key_update`.
    """

    def __init__(self, config, engine, categories, filelist):
        super().__init__(config, engine, categories, filelist)

    def _engine_load(self, batch_data):
        """
        Load the batch data into the MySQL database using upserts.

        Args:
            batch_data (list): A list of dictionaries representing the batch data.

        """
        grouped_data = defaultdict(list)
        for entry in batch_data:
            for category, data in entry.items():
                grouped_data[category].extend(data)

        with self.engine.connect() as conn:
            with conn.begin():
                logger.info("Loading batch into the database")

                for category, data in grouped_data.items():
                    table = get_table(category)
                    if table is None:
                        continue

                    stmt = mysql_insert(table).values(data).on_duplicate_key_update(**data)
                    conn.execute(stmt)


class SqliteDataLoader(DataLoader):
    """
    A data loader class for loading data into a SQLite database.

    This class extends the base DataLoader class and provides functionality
    to load data into a SQLite database using upsert (insert or replace) operation.

    Note: The upsert operation is achieved by using the "OR REPLACE" clause in the
    SQLite insert statement.
    """

    def __init__(self, config, engine, categories, filelist):
        super().__init__(config, engine, categories, filelist)

    def _engine_load(self, batch_data):
        grouped_data = defaultdict(list)
        for entry in batch_data:
            for category, data in entry.items():
                grouped_data[category].extend(data)

        with self.engine.connect() as conn:
            with conn.begin():
                logger.info("Loading batch into the database")

                for category, data in grouped_data.items():
                    table = get_table(category)
                    if table is None:
                        continue

                    stmt = sqlite_insert(table).values(data).prefix_with("OR REPLACE")
                    conn.execute(stmt)


class DataLoaderFactory:
    """
    Factory class for creating data loaders based on the database engine.
    """

    @staticmethod
    def get_loader(config, engine, categories, filelist):
        """
        Create a data loader based on the database engine.
        Args:
            config (dict): Configuration parameters for the data loader.
            engine (Engine): Database engine object.
            categories (list): List of categories to load.
            filelist (list): List of files to load.

        Returns:
            DataLoader: An instance of the appropriate data loader based on the database engine.

        Raises:
            NotImplementedError: If the database type is not supported.
        """
        if "mysql" in engine.url.drivername:
            return MysqlDataLoader(config, engine, categories, filelist)
        elif "sqlite" in engine.url.drivername:
            return SqliteDataLoader(config, engine, categories, filelist)
        else:
            raise NotImplementedError("Database type not supported")
