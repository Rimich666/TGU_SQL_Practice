import sys

from src.terminal.background import Back
from src.terminal.text import Text
from wait_key import Key


class ValueType(object):
    text = 'string',
    integer = 'integer',
    real = 'float',
    date = 'datetime'
    map = {
        'INTEGER': integer,
        'Datetime': date,
        'Utf8': text
    }
    check_map = {
        text: Key.chars,
        integer: Key.number,
        real: Key.number,
        date: Key.number
    }
    points = {
        text: [],
        integer: [],
        real: [1],
        date: [3, 6, 9, 12, 15, 18]
    }
    templ = {
        text: ' ',
        integer: '0',
        real: '0.0',
        date: '0001-01-01T00:00:00.000'
    }


class Mode(object):
    edit = 0,
    view = 1,
    choice = 2,
    action = 3


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
        after = 0 if self._align == Align.right else (self._width - len(text)) // self._align
        self._before = self._width - len(str(text)) - after
        return f"{self._before * ' '}{text}{after * ' '}"

    def active(self, is_active):
        self._param = self._active if is_active else self._not_active

    def align(self, align):
        self._align = align

    def on_enter(self):
        return self._value

    def value(self):
        return self._value


if __name__ == '__main__':
    w = 10
    ll = 4
    a = Align.center
