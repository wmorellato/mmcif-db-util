import os
import pytest
import shutil
import logging

from sqlalchemy import create_engine, MetaData, select

from mmcif_db_utils.config import Config
from mmcif_db_utils.data_loader import DataLoader
from mmcif_db_utils.models import database_2, create_tables

logger = logging.getLogger(__name__)


@pytest.fixture
def db_engine():
    engine = create_engine(f"sqlite:///test.db")
    yield engine
    engine.dispose()


@pytest.mark.integration
def test_data_load(db_engine):
    filelist = ["tests/fixtures/1o08.cif", "tests/fixtures/2gc2.cif"]
    with open("tests/fixtures/categories.txt") as fp:
        categories = fp.read().splitlines()
    create_tables(db_engine, categories=categories)
    loader = DataLoader(config=Config(), engine=db_engine, categories=categories, filelist=filelist)
    loader.load()

    with db_engine.connect() as conn:
        stmt = select(database_2.c.database_code)
        result = list(conn.execute(stmt))
        codes = list(map(lambda x: x[0], result))
        
        assert len(codes) == 2
        assert '1o08' in codes
        assert '2gc2' in codes
