import os
import re
import time
import click
import logging

from mmcif_db_utils.config import Config
from mmcif_db_utils.data_loader import DataLoaderFactory
from mmcif_db_utils.enums import DefaultSchemas
from mmcif_db_utils.models import drop_schema, create_tables, create_all_tables, metadata_obj

from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)


def get_category_list(cat_param):
    if os.path.exists(cat_param):
        with open(cat_param) as fp:
            return fp.read().splitlines()

    try:
        schema = DefaultSchemas(cat_param)
        return schema.get_category_list()
    except ValueError:
        raise ValueError(f"Invalid schema: {cat_param}")


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
    CATEGORIES is either:
        - A file containing a list of categories to load, separated by newlines.
        - One of 'compv4', 'da_internal', 'pdbe_all'.
    FILELIST is a file containing a list of absolute paths to mmCIF files to load, separated by newlines
    """
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger("pdbe_db_loader.data_loader").setLevel(logging.DEBUG)

    click.echo(f"Loading model data into {re.sub(r':.*@', ':****@', db_url)}")

    try:
        clist = get_category_list(categories)
    except ValueError as e:
        click.echo("You didn't provide a valid schema or file. Valid schemas are: 'compv4', 'da_internal', 'pdbe_all'")
        return

    if not os.path.exists(filelist):
        click.echo(f"Filelist {filelist} not found")
        return

    with open(filelist) as fp:
        flist = fp.read().splitlines()

    config = Config()
    engine = create_engine(db_url)
    loader = DataLoaderFactory.get_loader(config, engine, clist, flist)
    start = time.time()
    loader.load()
    end = time.time()
    click.echo(f"Data loaded in {end - start:.2f} seconds")


@click.command()
@click.argument("db_url")
@click.argument("categories")
@click.option("--drop", "-d", flag_value=True, help="Drop schema before creating")
@click.option("--verbose", "-v", flag_value=True, help="Verbose output")
def create_schemas(db_url, categories, drop, verbose):
    """Create database schema for CATEGORIES in database
    described by DB_URL.

    DB_URL is a connection string in the format mysql+pymysql://user:password@host:port/dbname
    CATEGORIES is a file containing a list of categories to load, separated by newlines
    """
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger("pdbe_db_loader.data_loader").setLevel(logging.DEBUG)

    try:
        engine = create_engine(db_url)

        if drop:
            logging.info(f"Dropping schema in {re.sub(r':.*@', ':****@', db_url)}")
            drop_schema(engine)

        if categories == "all":
            create_all_tables(engine)
            click.echo(f"Created all tables in {re.sub(r':.*@', ':****@', db_url)}")
            return

        with open(categories) as fp:
            categories = fp.read().splitlines()
            create_tables(engine, categories)
            click.echo(f"Created tables in {re.sub(r':.*@', ':****@', db_url)}")
    except Exception as e:
        click.echo(f"Error creating schemas. Set the verbose flag to see more information")

        if verbose:
            logging.error(e)


cli.add_command(load)
cli.add_command(create_schemas)


if __name__ == '__main__':
    cli()
