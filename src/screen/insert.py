from src.base.pragma import get_fields
from src.screen.screen import Screen


class Insert(Screen):
    def __init__(self, table):
        super().__init__()
        self._table = table
        self._fields = get_fields(table)
        self._headers = self._fields[0]
        self._widths = self._fields[1]
        self.lines = self.make_lines(self._fields[2:])
        self.lines.append(('Назад',))
        self.make_header()
