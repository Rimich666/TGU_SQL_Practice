import datetime

from src.cell.cell import Align
from src.cell.edit_cell.edit_cell import EditCell
from wait_key import Key


class DateCell(EditCell):
    def __init__(self, value, width):
        super().__init__(value, width)
        self._templ = '0001-01-01T00:00:00.000'
        self._current_text = value if value else datetime.datetime.now().isoformat()[:23]
        self._cursor_pos = 0
        self._align = Align.right
        self.check_keys = Key.integer
        self._fields = ['0', '1']

    def on_key(self, key):
        if self._templ[self._cursor_pos] in self._fields:
            text = self._current_text
            pos = self._cursor_pos
            self._current_text = text[: pos] + key + text[pos + 1:]
            if self._cursor_pos < len(self._current_text) - 1:
                diff = 1 if text[pos + 1] in self._fields else 2
                self._cursor_pos += diff

    def backspace(self):
        pass

    def delete(self):
        if self._templ[self._cursor_pos] in self._fields:
            text = self._current_text
            pos = self._cursor_pos
            self._current_text = text[: pos] + self._templ[pos] + text[pos + 1:]


if __name__ == '__main__':
    print()
