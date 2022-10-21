from collections import OrderedDict
from typing import List, Optional

from dedoc.data_structures.cell_property import CellProperty
from dedoc.data_structures.table_metadata import TableMetadata


class Table:

    def __init__(self, cells: List[List[str]]) -> None:

        self.cells = [[cell_text for cell_text in row] for row in cells]

    def to_dict(self) -> dict:
        res = OrderedDict()
        res["cells"] = [[cell_text for cell_text in row] for row in self.cells]
        return res
