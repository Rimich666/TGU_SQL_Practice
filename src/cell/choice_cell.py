import json

from src.base.database import log
from src.cell.cell import Cell


class ChoiceCell(Cell):
    def __init__(self, props, width):
        value, self._fk = props
        log(f'init: {json.dumps(self._fk)}')
        super().__init__(value, width)

    @property
    def table(self):
        log(f'property table: {json.dumps(self._fk)}')
        return self._fk['table']
