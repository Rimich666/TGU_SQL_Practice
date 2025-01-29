import sys

from src.terminal.background import Back
from src.terminal.text import Text


class Screen(object):
    def __init__(self, on_enter=None):
        self.current_line = 0
        self.current_column = 0
        self.on_enter = on_enter
        self._fields = []
        self._widths = ()
        self._headers = ()
        self._title = None
        self._header = None
        self._footer = None
        self._lines = []

    def print(self):
        sys.stdout.write(Back.default + Text.default)
        if self._title:
            print(self._title + '\n')
        if self._header:
            print(self._header)
        for i, line in enumerate(self._lines):
            sys.stdout.write(Back.default + Text.default + f'{i} ')
            for j, value in enumerate(line):
                if i == self.current_line and j == self.current_column:
                    sys.stdout.write(Back.white + Text.black)
                else:
                    sys.stdout.write(Back.default + Text.default)
                sys.stdout.write(f'{value} ')
            sys.stdout.write('\n')
        sys.stdout.write(Back.default + Text.default)

    def change_line(self, direction):
        self.current_line = (self.current_line + direction) % len(self._lines)
        line_end = len(self._lines[self.current_line]) - 1
        if self.current_column > line_end:
            self.current_column = line_end

    def down(self):
        self.change_line(1)

    def up(self):
        self.change_line(-1)

    def right(self):
        self.current_column = (self.current_column + 1) % len(self._lines[self.current_line])

    def left(self):
        self.current_column = (self.current_column - 1) % len(self._lines[self.current_line])

    def enter(self):
        pass

    def make_header(self):
        def get_head(val, length):
            len_val = len(str(val))
            before = (length - len_val) // 2
            after = length - len_val - before
            return f"{before * '_'}{val}{after * '_'}"

        if self._fields:
            headers = [get_head(self._headers[i], self._widths[i]) for i in range(len(self._widths))]
            headers.insert(0, get_head('№', len(str(len(self._fields) - 1))))
            self._header = ' '.join(headers)
        else:
            self._header = None

    def make_lines(self, rows):

        def get_cell(val, length):
            is_numeric = type(val) is float or (type(val) is int)
            len_val = len(str(val))
            before = length - len_val if is_numeric else 0
            after = length - len_val - before
            return f"{before * ' '}{val}{after * ' '}"

        return list(map(lambda row: list([get_cell(row[i], self._widths[i]) for i in range(len(row))]), rows))


if __name__ == '__main__':
    n = 1
    print(type(n) is int)
    m = 1.5
    print(type(m) is float or (type(m) is int))
