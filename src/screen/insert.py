from src.base.pragma import get_fields
from src.screen.screen import Screen


class Insert(Screen):
    def __init__(self, table):
        super().__init__()
        self._table = table
        self._fields = get_fields(table)
        self._headers = self._fields[0]
        self._widths = self._fields[1]
        self._lines = self.make_lines(self._fields[2:])
        self._lines.append(('Назад',))
        self.make_header()

    def make_header(self):
        super().make_header()
        self._header = f"{self._headers} {' ' * 10}value{' ' * 10}"

    def make_lines(self, rows):
        lines = list(map(lambda line: line + [f"{' ' * 25}"], super().make_lines(rows)))
        return lines
