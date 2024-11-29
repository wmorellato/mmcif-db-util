import os
import re
import time
import click
import logging

from mmcif_db_utils.config import Config
from mmcif_db_utils.data_loader import DataLoader

from sqlalchemy import create_engine
from wwpdb.utils.config.ConfigInfo import ConfigInfo

logging.basicConfig(level=logging.INFO)


@click.group()
def cli():
    pass


@click.command()
@click.argument("db_url")
@click.argument("categories")
@click.argument("filelist")
@click.option("--verbose", flag_value=True, help="Verbose output")
def load(db_url, categories, filelist, verbose):
    """Load data for CATEGORIES from entries in FILELIST
    into the database described by DB_URL.

    DB_URL is a connection string in the format mysql+pymysql://user:password@host:port/dbname    
    CATEGORIES is a file containing a list of categories to load, separated by newlines
    FILELIST is a file containing a list of absolute paths to mmCIF files to load, separated by newlines
    """
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger("pdbe_db_loader.data_loader").setLevel(logging.DEBUG)

    click.echo(f"Loading model data into {re.sub(r':.*@', ':****@', db_url)}")

    config = Config()
    engine = create_engine(db_url)
    loader = DataLoader(config=config, engine=engine)
    start = time.time()
    loader.load()
    end = time.time()
    click.echo(f"Data loaded in {end - start:.2f} seconds")


@click.command()
@click.argument("db_url")
@click.argument("categories")
@click.option("--verbose", flag_value=True, help="Verbose output")
def create_schemas(db_url, categories):
    """Create database schema for CATEGORIES in database
    described by DB_URL.

    DB_URL is a connection string in the format mysql+pymysql://user:password@host:port/dbname    
    CATEGORIES is a file containing a list of categories to load, separated by newlines
    """
    engine = create_engine(db_url)
    config = Config()
    loader.setup_schema()


cli.add_command(load)
cli.add_command(create_schemas)


if __name__ == '__main__':
    cli()
