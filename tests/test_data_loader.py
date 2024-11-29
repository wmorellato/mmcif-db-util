import os
import pytest
import shutil
import logging

from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import Session

from mmcif_db_utils.config import Config
from mmcif_db_utils.data_loader import DataLoader

logger = logging.getLogger(__name__)


# def test_parse_cc_file():
#     reader = ChemCompReader(config=Config())
#     data = reader.read('./tests/fixtures/MIL.cif')

#     assert '_chem_comp' in data
#     assert '_chem_comp_atom' in data
#     assert '_chem_comp_bond' in data
#     assert '_pdbx_chem_comp_descriptor' in data
#     assert '_pdbx_chem_comp_identifier' in data
#     assert '_pdbx_chem_comp_audit' in data


@pytest.fixture
def db_engine():
    engine = create_engine("sqlite+pysqlite:///:memory:")
    yield engine
    engine.dispose()


@pytest.mark.integration
def test_schema_creation(db_engine, tmp_path):
    config = Config()
    filelist = ["fixtures/1o08.cif", "fixtures/2gc2.cif"]
    categories = "fixtures/categories.txt"
    loader = DataLoader(config=config, engine=db_engine, filelist=tmp_path, categories=tmp_path)
    loader.load()

    with db_engine.connect():
        meta = MetaData()
        meta.reflect(bind=db_engine)

        for table in config.chem_comp_categories:
            assert table.lstrip("_") in meta.tables


# @pytest.mark.integration
# def test_schema_recreation(db_engine, tmp_path):
#     config = Config()
#     loader = DataLoader(config=config, engine=db_engine, ccd_root=tmp_path)
#     loader.load()
#     loader.load()


# @pytest.mark.integration
# def test_data_load(ligand_dict, db_engine):
#     loader = DataLoader(config=Config(), engine=db_engine, ccd_root=ligand_dict)
#     loader.load()

#     with db_engine.connect() as conn:
#         stmt = select(chem_comp.c.id)
#         result = list(conn.execute(stmt))
#         codes = list(map(lambda x: x[0], result))
        
#         assert len(codes) == 4
#         assert '001' in codes
#         assert 'ABC' in codes
#         assert 'MIL' in codes
#         assert 'TON' in codes
