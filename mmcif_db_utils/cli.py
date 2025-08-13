import os
import re
import sys
import time
import click
import logging

from mmcif_db_utils.config import Config
from mmcif_db_utils.data_loader.loader import DataLoaderFactory
from mmcif_db_utils.data_loader.enums import DefaultSchemas
from mmcif_db_utils.data_loader.models import drop_schema, create_tables
from mmcif_db_utils.schema.printers import SqlAlchemyOrmPrinter, SqlAlchemyCorePrinter
from mmcif_db_utils.schema.mmcif_dict import DictReader, ItemFilter
from mmcif_db_utils.schema.mappings import SchemaMap

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


def get_printer(model, include_imports, fp=None):
    if model == "orm":
        return SqlAlchemyOrmPrinter(fp=fp, include_imports=include_imports)
    elif model == "core":
        return SqlAlchemyCorePrinter(fp=fp, include_imports=include_imports)


def get_filtered_items(path):
    with open(path) as f:
        return set([line.strip() for line in f])


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
        click.echo("You didn't provide a valid schema or file with categories. Valid schemas are: 'compv4', 'da_internal', 'pdbe_all'")
        return

    if not os.path.exists(filelist):
        click.echo(f"Filelist {filelist} not found")
        return

    with open(filelist) as fp:
        flist = fp.read().splitlines()

    config = Config()
    engine = create_engine(db_url, future=True)
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
    CATEGORIES is either:
        - A file containing a list of categories to load, separated by newlines.
        - One of 'compv4', 'da_internal', 'pdbe_all'.
    """
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger("pdbe_db_loader.data_loader").setLevel(logging.DEBUG)

    try:
        engine = create_engine(db_url)

        if drop:
            logging.info(f"Dropping schema in {re.sub(r':.*@', ':****@', db_url)}")
            drop_schema(engine)

        try:
            categories = get_category_list(categories)
        except ValueError as e:
            click.echo("You didn't provide a valid schema or file with categories. Valid schemas are: 'compv4', 'da_internal', 'pdbe_all'")
            return

        create_tables(engine, categories)
        click.echo(f"Created tables in {re.sub(r':.*@', ':****@', db_url)}")
    except Exception as e:
        click.echo(f"Error creating schemas. Set the verbose flag to see more information")

        if verbose:
            logging.error(e)


@click.command()
@click.argument("mmcif_dictionary", type=click.Path())
@click.argument("categories")
@click.option("--model", type=str, default="orm", help="Choose between 'orm' and 'core' models")
@click.option("--include-items-file", type=click.Path(), help="Path to the file containing the list of categories and items to be included. The file have one 'category_name.item_name' per line. Any item not included in the file will be ignored. Cannot be used with --exclude-items-file.")
@click.option("--exclude-items-file", type=click.Path(), help="Path to the file containing the list of categories and items to be included. The file have one 'category_name.item_name' per line. Any item not included in the file will be processed. Cannot be used with --include-items-file.")
@click.option("--output-file", type=click.Path(), help="Path to the output file")
@click.option("--verbose", "-v", is_flag=True, help="Print debug messages")
def create_model(mmcif_dictionary, categories, model, include_items_file, exclude_items_file, output_file, verbose):
    """Create SQLAlchemy models for categories based on the
    input MMCIF_DICTIONARY.

    CATEGORIES is either:
    - A file containing a list of categories to load, separated by newlines.
    - One of 'compv4', 'da_internal', 'pdbe_all'.
    """
    included_items = []
    excluded_items = []

    if verbose:
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger("mmcif_dict").setLevel(logging.DEBUG)

    cr = DictReader(path=mmcif_dictionary)

    if include_items_file and exclude_items_file:
        raise click.UsageError("These options are mutually exclusive: --include-items-file, --exclude-items-file")

    try:
        categories = get_category_list(categories)
    except ValueError as e:
        click.echo("You didn't provide a valid schema or file with categories. Valid schemas are: 'compv4', 'da_internal', 'pdbe_all'")
        return

    if include_items_file:
        included_items = get_filtered_items(include_items_file)

    if exclude_items_file:
        excluded_items = get_filtered_items(exclude_items_file)

    filter = ItemFilter(include_items=included_items, exclude_items=excluded_items)
    cat_objs = cr.get_categories(categories=categories, filter=filter)

    with open(output_file, "w") if output_file else sys.stdout as f:
        mp = get_printer(model, include_imports=True, fp=f)
        sm = SchemaMap(printer=mp, ignore_relationships=True)
        sm.add_categories(cat_objs)
        sm.print_models()


cli.add_command(load)
cli.add_command(create_schemas)
cli.add_command(create_model)


if __name__ == '__main__':
    cli()
