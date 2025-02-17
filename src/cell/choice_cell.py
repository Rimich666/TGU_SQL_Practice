import json

from src.base.database import log
from src.cell.cell import Cell


class ChoiceCell(Cell):
    def __init__(self, props, width):
        value, self._fk, self._name = props
        super().__init__(value, width)
        print(self._name)

    @property
    def table(self):
        log(f'property table: {json.dumps(self._fk)}')
        return self._fk['table']

    @property
    def name(self):
        return self._name
