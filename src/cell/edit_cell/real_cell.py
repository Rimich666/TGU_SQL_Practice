from src.cell.Align import Align
from src.cell.edit_cell.edit_cell import EditCell
from wait_key import Key


class RealCell(EditCell):
    def __init__(self, value, width):
        super().__init__(value, width)
        val = str(value) if value else ' .'
        point = val.find('.')
        self._current_text = val if point > -1 else val + '.'
        self._point = self._current_text.index('.')
        self._cursor_pos = self._point - 1
        self._align = Align.right
        self.check_keys = Key.integer

    def on_key(self, key):
        if len(self._current_text) < self._width:
            if self._current_text[self._cursor_pos] == '.':
                self._current_text += key
                self._cursor_pos = len(self._current_text) - 1
            else:
                head = self._current_text[:self._cursor_pos + 1]
                tail = self._current_text[self._cursor_pos + 1:]
                self._current_text = head + key + tail
                self._cursor_pos += 1

    def backspace(self):
        pass

    def delete(self):
        if self._current_text[self._cursor_pos] == '.':
            return
        head = self._current_text[:self._cursor_pos]
        tail = self._current_text[self._cursor_pos + 1:]
        self._current_text = head + tail
        if self._cursor_pos > 0 or not self._current_text:
            self._cursor_pos -= 1
