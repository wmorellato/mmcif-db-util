# MMCIF DB Utils CLI

This CLI tool is designed to load data from mmCIF files into a database. It supports various schemas and can be configured for verbose output.

## Installation

To install the package, you can use `pip`:

```sh
pip install mmcif-db-utils
```

## Usage

The CLI provides a command to load data into a database. Below is the usage information.

### Load

```
mmcif-db-utils load [OPTIONS] DB_URL CATEGORIES FILELIST
```

#### Arguments

- `DB_URL`: The database connection string in the format mysql+pymysql://user:password@host:port/dbname.
- `CATEGORIES`: Either a file containing a list of categories to load (one per line) or one of the predefined schemas (compv4, da_internal, pdbe_all).
- `FILELIST`: A file containing a list of absolute paths to mmCIF files to load (one per line).

#### Options
- `--verbose`: Enable verbose output for debugging purposes.

#### Example

```
mmcif-db-utils load mysql+pymysql://user:password@localhost:3306/mydatabase categories.txt|schema filelist.txt [--verbose]
```

