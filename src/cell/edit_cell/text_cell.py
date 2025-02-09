from log import LOG
from src.cell.cell import Align
from src.cell.edit_cell.edit_cell import EditCell
from wait_key import Key


class TextCell(EditCell):
    def __init__(self, value, width):
        super().__init__(value, width)
        self._current_text = str(value) + '_'
        self._cursor_pos = len(self._current_text) - 1
        self._align = Align.left
        self.check_keys = Key.chars

    def delete(self):
        if self._cursor_pos < len(self._current_text) - 1:
            head = self._current_text[:self._cursor_pos]
            tail = self._current_text[self._cursor_pos + 1:]
            self._current_text = head + tail

    def left(self):
        if self._cursor_pos > 0:
            self._cursor_pos -= 1

    def right(self):
        if self._cursor_pos < len(self._current_text) - 1:
            self._cursor_pos += 1

    def on_key(self, key):
        super().on_key(key)
        self._cursor_pos += 1

    def _text(self, text):
        if len(text) <= self._width:
            return super()._text(text)
        if self._width <= self._cursor_pos < len(text):
            return text[self._cursor_pos - self._width + 1: self._cursor_pos + 1]
        return text[: self._width]
