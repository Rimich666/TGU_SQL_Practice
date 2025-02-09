from src.base.pragma import get_fields
from src.cell.cell import ValueType
from src.cell.edit_cell.make_edit_cell import make_edit_cell
from src.screen.screen import Screen


class Insert(Screen):
    def __init__(self, table, actions):
        super().__init__()
        self._table = table
        self._fields = get_fields(table)
        self._headers = self._fields[0]
        self._widths = self._fields[1]
        self._actions = actions
        self._lines = self.make_lines(self._fields[2:])
        super().set_actions()
        self.make_header()

    def make_header(self):
        super().make_header()
        self._header = f"{self._headers} {' ' * 10}value{' ' * 10}"

    # def make_lines(self, rows):
    #     lines = super().make_lines(rows)
    #     obj = make_edit_cell(
    #                 '', 25, ValueType.map[lines[0][1].value()]
    #                 )
    #     LOG[0] = f'{obj}'
    #     lines = list(map(lambda line: line + [
    #         TextCell(
    #             '', 25
    #         )], super().make_lines(rows)))
    #     return lines

    def make_lines(self, rows):
        lines = list(map(lambda line: line + [make_edit_cell(
            '', 10, ValueType.map[line[1].value()]
            )], super().make_lines(rows)))
        return lines
