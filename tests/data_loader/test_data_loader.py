import os
import pytest
import logging

from sqlalchemy import create_engine, select

from mmcif_db_utils.config import Config
from mmcif_db_utils.data_loader.loader import DataLoaderFactory
from mmcif_db_utils.data_loader.models import database_2, create_tables

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine("sqlite+pysqlite:///test.db")
    yield engine
    engine.dispose()
    os.remove("test.db")


@pytest.mark.integration
def test_data_load(db_engine):
    filelist = ["tests/fixtures/1o08.cif", "tests/fixtures/2gc2.cif"]
    with open("tests/fixtures/categories.txt") as fp:
        categories = fp.read().splitlines()
    create_tables(db_engine, categories=categories)
    loader = DataLoaderFactory.get_loader(Config(), db_engine, categories, filelist)
    loader.load()

    with db_engine.connect() as conn:
        stmt = select(database_2.c.database_code).where(database_2.c.database_id == "PDB")
        result = list(conn.execute(stmt))
        codes = list(map(lambda x: x[0], result))
        
        assert len(codes) == 2
        assert "1O08" in codes
        assert "2GC2" in codes
