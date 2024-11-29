import os
import pytest
import shutil
import logging

from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import Session

from mmcif_db_utils.config import Config
from mmcif_db_utils.models import create_all_tables, create_tables

logger = logging.getLogger(__name__)


@pytest.fixture
def db_engine():
    engine = create_engine("sqlite+pysqlite:///:memory:")
    yield engine
    engine.dispose()


@pytest.mark.integration
def test_create_tables(db_engine):
    with open("tests/fixtures/categories.txt") as f:
        categories = f.read().splitlines()

    create_tables(db_engine, categories)

    with db_engine.connect():
        meta = MetaData()
        meta.reflect(bind=db_engine)

        for table in categories:
            assert table in meta.tables
