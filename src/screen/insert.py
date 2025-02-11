from src.base.pragma import get_fields
from src.cell.cell import ValueType
from src.cell.edit_cell.make_edit_cell import make_edit_cell
from src.screen.screen import Screen


class Insert(Screen):
    def __init__(self, table, actions):
        super().__init__()
        self._table = table
        self._fields = get_fields(table, False)
        self._headers = self._fields[0]
        self._widths = self._fields[1]
        self._actions = actions
        self._lines = self.make_lines(self._fields[2:])
        super().set_actions()
        self.make_header()

    def make_header(self):
        super().make_header()
        self._header += [f"{' ' * 10}value{' ' * 10}"]

    def make_lines(self, rows):
        lines = list(map(lambda line: line + [make_edit_cell(
            '', 25, ValueType.map[line[1].value]
            )], super().make_lines(rows)))
        return lines

    def get_values(self):
        fields = {item[0].value: item[len(self._fields[0])].value for item in self._lines[:len(self._fields) - 2]}
        return {
            'table': self._table,
            'fields': fields
        }
