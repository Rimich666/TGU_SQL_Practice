import sys

from src.cell.cell import Cell, Mode
from wait_key import Key


class EditCell(Cell):
    def __init__(self, value, width):
        super().__init__(value, width)
        self._edit_mode = Mode.view
        self._current_text = ''
        self._cursor_pos = 0
        self.mode = Mode.view
        self.check_keys = Key.control

    def backspace(self):
        if self._cursor_pos > 0:
            head = self._current_text[:self._cursor_pos - 1]
            tail = self._current_text[self._cursor_pos:]
            self._current_text = head + tail
            self._cursor_pos -= 1

    def left(self):
        if self._cursor_pos > 0:
            self._cursor_pos -= 1

    def right(self):
        if self._cursor_pos < len(self._current_text) - 1:
            self._cursor_pos += 1

    def home(self):
        self._cursor_pos = 0

    def end(self):
        self._cursor_pos = len(self._current_text) - 1

    def on_key(self, key):
        pass

    def delete(self):
        pass

    def enter(self):
        self._value = self._current_text.strip()
        self.mode = Mode.view

    def clear(self):
        self._value = ''

    def on_press(self, key_name):
        if key_name in Key.edit:
            getattr(self, key_name)()
        else:
            self.on_key(key_name)
        return self.mode == Mode.view

    def print(self):
        if self.mode == Mode.view:
            super().print()
        else:
            text = self._text(self._current_text)
            pos = self._cursor_pos + self._before if self._cursor_pos < self._width - 1 else self._width - 1
            head = text[:pos]
            tail = text[pos + 1:]
            sys.stdout.write(head)
            self._param.print()
            sys.stdout.write(text[pos])
            self._default.print()
            sys.stdout.write(tail)

    def on_enter(self):
        self.mode = Mode.edit
