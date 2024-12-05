from enum import Enum

import importlib.resources as pkg_resources

from mmcif_db_utils import data


class DefaultSchemas(Enum):
    COMPV4 = "compv4"
    DA_INTERNAL = "da_internal"
    PDBE_ALL = "pdbe_all"

    def get_category_list(self):
        with pkg_resources.open_text(data, f"{self.value}.txt") as fp:
            return fp.read().splitlines()
