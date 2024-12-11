import sys

ORM_IMPORTS = [
    "from typing import List", 
    "from typing import Optional", 
    "from sqlalchemy import ForeignKey", 
    "from sqlalchemy import String", 
    "from sqlalchemy.orm import DeclarativeBase", 
    "from sqlalchemy.orm import Mapped", 
    "from sqlalchemy.orm import mapped_column", 
    "from sqlalchemy.orm import relationship", 
]

CORE_IMPORTS = [
    "from sqlalchemy import MetaData, Table, Column, Integer, String, Float, Date, DateTime"
]

ORM_SETUP = ["class Base(DeclarativeBase):", "    pass"]

CORE_SETUP = ["metadata_obj = MetaData()"]


def snakecase_to_camelcase(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)


class SqlAlchemyCorePrinter:
    def __init__(self, fp = sys.stdout, include_imports=False):
        self._fp = fp
        self._include_imports = include_imports
        self._tables = []

    def add_table(self, table):
        self._tables.append(table)
    
    def _column_text(self, column):
        params = []
        if column.index:
            params.append("primary_key=True")
        if column.nullable:
            params.append(f"nullable={column.nullable}")
        if column.default is not None:
            if isinstance(column.default, str):
                params.append(f'default="{column.default}"')
            else:
                params.append(f'default={column.default}')

        params_str = ", ".join(params)
        if params_str:
            return f'Column("{column.name}", {column.subtype}, {params_str})'
        else:
            return f'Column("{column.name}", {column.subtype})'

    def _table_text(self, table):
        columns = []
        for column in table.columns:
            columns.append(f"    {self._column_text(column)}")

        return f'{table.name} = Table("{table.name}",\n    metadata_obj,\n' + ",\n".join(columns) + "\n)"

    def print(self):
        if self._include_imports:
            for i in CORE_IMPORTS:
                self._fp.write(i + "\n")
            self._fp.write("\n\n")

        for i in CORE_SETUP:
            self._fp.write(i + "\n")
        self._fp.write("\n\n")

        for table in self._tables:
            self._fp.write(self._table_text(table) + "\n")
            self._fp.write("\n\n")


class SqlAlchemyOrmPrinter:
    def __init__(self, fp = sys.stdout, include_imports=False):
        self._fp = fp
        self._include_imports = include_imports
        self._tables = []

    def add_table(self, table):
        self._tables.append(table)

    def _column_text(self, column):
        params = []
        if column.index:
            params.append("primary_key=True")
        if column.type == "str":
            params.append(f"type_={column.subtype}")
        if column.default is not None:
            if isinstance(column.default, str):
                params.append(f'default="{column.default}"')
            else:
                params.append(f'default={column.default}')

        params_str = ", ".join(params)
        if column.nullable:
            return f'{column.name}: Mapped[Optional[{column.type}]] = mapped_column({params_str})'
        else:
            return f'{column.name}: Mapped[{column.type}] = mapped_column({params_str})'

    def _table_text(self, table):
        class_name = snakecase_to_camelcase(table.name)
        class_template = f"""class {class_name}(Base):
    __tablename__ = '{table.name}'\n\n"""
        
        for column in table.columns:
            class_template += f"    {self._column_text(column)}\n"

        return class_template

    def print(self):
        if self._include_imports:
            for i in ORM_IMPORTS:
                self._fp.write(i + "\n")
            self._fp.write("\n\n")

        for i in ORM_SETUP:
            self._fp.write(i + "\n")
        self._fp.write("\n\n")

        for table in self._tables:
            self._fp.write(self._table_text(table) + "\n\n")
