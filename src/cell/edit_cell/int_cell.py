from src.cell.Align import Align
from src.cell.edit_cell.edit_cell import EditCell
from wait_key import Key


class IntCell(EditCell):
    def __init__(self, value, width):
        super().__init__(value, width)
        self._current_text = str(value)
        self._cursor_pos = len(self._current_text) - 1
        self._align = Align.right
        self.check_keys = Key.integer

    def on_key(self, key):
        if len(self._current_text) < self._width:
            head = self._current_text[:self._cursor_pos + 1]
            tail = self._current_text[self._cursor_pos + 1:]
            self._current_text = head + key + tail
            self._cursor_pos += 1

    def delete(self):
        head = self._current_text[:self._cursor_pos]
        tail = self._current_text[self._cursor_pos + 1:]
        self._current_text = head + tail
        if self._cursor_pos > 0 or not self._current_text:
            self._cursor_pos -= 1
