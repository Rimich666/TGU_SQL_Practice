import sys

from src.cell.Align import Align
from src.terminal.background import Back
from src.terminal.text import Text


class Mode(object):
    edit = 0,
    view = 1,
    choice = 2,
    action = 3


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
        self._before = 0
        self._not_active = CellParam()
        self._active = CellParam(Text.black, Back.white)
        self._param = self._not_active
        self._default = CellParam()
        self.mode = Mode.view

    def print(self):
        self._param.print()
        sys.stdout.write(self._text(self._value))
        self._default.print()

    def _text(self, text):
        if self._width == 0:
            return text
        after = 0 if self._align == Align.right else (self._width - len(str(text))) // self._align
        self._before = self._width - len(str(text)) - after
        return f"{self._before * ' '}{text}{after * ' '}"

    def active(self, is_active):
        self._param = self._active if is_active else self._not_active

    @property
    def align(self):
        return self._align

    @align.setter
    def align(self, align):
        self._align = align

    def on_enter(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


if __name__ == '__main__':
    w = 10
    ll = 4
    a = Align.center
