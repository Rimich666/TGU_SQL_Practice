import sys

from src.cell.cell import Cell, Mode, ValueType, Align
from wait_key import Key


class EditCell(Cell):
    def __init__(self, value, width, value_type=ValueType.text):
        super().__init__(value, width)
        self._edit_mode = Mode.view
        self._type = value_type
        self._set_cursor_pos()
        self.mode = Mode.view
        self._align = Align.map[self._type]

    def _set_cursor_pos(self):
        if self._type == ValueType.text:
            self._cursor_pos = len(self.value())
        elif self._type == ValueType.integer or self._type == ValueType.real:
            self._cursor_pos = len(self.value()) - 1
        elif self._type == ValueType.date:
            self._cursor_pos = 0

    def on_press(self, key):
        if key not in Key.edit:
            self._value = self._value + key

    def type(self):
        return self._type

    def print(self):
        if self.mode == Mode.view:
            super().print()
        else:
            text = self._text() + ' '
            sys.stdout.write(text[:self._cursor_pos])
            self._param.print()
            sys.stdout.write(text[self._cursor_pos])
            self._default.print()
            sys.stdout.write(text[self._cursor_pos:])

    def enter(self):
        self.mode = Mode.edit
    #     "YYYY-MM-DD HH:MM:SS.SSS"
    #     pass
