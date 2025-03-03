from src.base.pragma import get_fields
from src.cell.value_type import ValueType
from src.cell.edit_cell.check_cell import CheckCell
from src.cell.edit_cell.make_edit_cell import make_edit_cell
from src.screen.screen import Screen


class Select(Screen):
    def __init__(self, table, actions):
        super().__init__(actions=actions)
        print(table)
        self._table = table
        self._title = f'Создание запроса к таблице "{self._table}"'
        self._fields, _ = get_fields(table, True)
        self.set_fields()

    def make_header(self):
        super().make_header()
        self._header += ["select", f"{' ' * 10}where{' ' * 10}"]

    def make_lines(self, rows):
        lines = list(map(lambda line: line + [CheckCell()] + [make_edit_cell(
            '', 25, ValueType.map[line[1].value]
            )], super().make_lines(rows)))
        return lines

    def get_values(self):
        select = {item[0].value: item[len(self._fields[0])].value for item in self._lines[:len(self._fields) - 2]}
        where = {item[0].value: item[len(self._fields[0]) + 1].value for item in self._lines[:len(self._fields) - 2]}
        return {
            'table': self._table,
            'select': select,
            'where': where
        }
