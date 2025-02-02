import sys

from src.terminal.background import Back
from src.terminal.text import Text


class Align(object):
    left = 1
    center = 2
    right = 0


class CellParam(object):
    def __init__(self, color=Text.white, background=Back.black, bold=Text.thin):
        self._color = color
        self._background = background
        self._bold = bold

    def print(self):
        sys.stdout.write(self._color + self._background + self._bold)


class Cell(object):
    def __init__(self, value, width=0):
        self._value = value
        self._align = Align.left
        self._width = width
        self._not_active = CellParam()
        self._active = CellParam(Text.black, Back.white)
        self._param = self._not_active
        self._default = CellParam()

    def print(self):
        self._param.print()
        sys.stdout.write(self._text())
        self._default.print()

    def _text(self):
        if self._width == 0:
            return self._value
        after = 0 if self._align == Align.right else (self._width - len(self._value)) // self._align
        before = self._width - len(str(self._value)) - after
        return f"{before * ' '}{self._value}{after * ' '}"

    def active(self, is_active):
        self._param = self._active if is_active else self._not_active

    def align(self, align):
        self._align = align

    def enter(self):
        return self._value


if __name__ == '__main__':
    w = 10
    ll = 4
    a = Align.center
