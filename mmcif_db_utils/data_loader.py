import os
import queue
import logging

from typing import List
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

from gemmi import cif

from mmcif_db_utils.schemas import Status, ExperimentTypes
from mmcif_db_utils.models import get_table, cast_type, metadata_obj

logger = logging.getLogger(__name__)


class ModelFileReader:
    def __init__(self, config, categories):
        self.config = config
        self.categories = categories
    
    def _table_to_dict(self, category, table):
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


class DataLoader:
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

    def _load_multi(self, batch_data):
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

                    stmt = table.insert(prefixes=["IGNORE"]).on_conflict_do_nothing()
                    conn.execute(stmt, data)

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
                    self._load_multi(db_batch)
                except Exception as e:
                    logger.error(f"Error loading data for worker {worker} from {file}: {str(e)}")
                finally:
                    db_batch.clear()

        if db_batch:
            logger.info(f"Loading remaining data for worker {worker}")

            try:
                self._load_multi(db_batch)
            except Exception as e:
                logger.error(f"Error loading remaining data for worker {worker}: {str(e)}")
            finally:
                db_batch.clear()

    def load(self):
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
