import sys

from src.cell.action_cell import ActionCell
from src.cell.cell import Cell, Align
from src.terminal.background import Back
from src.terminal.text import Text


class Screen(object):
    def __init__(self, on_enter=None, actions=None):
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
        self._actions = actions

    def set_actions(self):
        if self._actions is not None:
            for action in self._actions:
                self._lines.append([ActionCell(*action)])
        self._lines[0][0].active(True)

    def print(self):
        sys.stdout.write(Back.default + Text.default)
        if self._title:
            print(self._title + '\n')
        if self._header:
            print(self._header)
        for i, line in enumerate(self._lines):
            sys.stdout.write(Back.default + Text.default + f'{i} ')
            for cell in line:
                cell.print()

            sys.stdout.write('\n')
        sys.stdout.write(Back.default + Text.default)

    def change_cell(self, line_direction=0, column_direction=0):
        self._lines[self.current_line][self.current_column].active(False)
        self.current_line = (self.current_line + line_direction) % len(self._lines)
        self.current_column = (self.current_column + column_direction) % len(self._lines[self.current_line])
        line_end = len(self._lines[self.current_line]) - 1
        if self.current_column > line_end:
            self.current_column = line_end
        self._lines[self.current_line][self.current_column].active(True)

    def down(self):
        self.change_cell(line_direction=1)

    def up(self):
        self.change_cell(line_direction=-1)

    def right(self):
        self.change_cell(column_direction=1)

    def left(self):
        self.change_cell(column_direction=-1)

    def enter(self):
        cell = self._lines[self.current_line][self.current_column]
        if isinstance(cell, ActionCell):
            cell.enter()
        else:
            self.on_enter(cell.enter())

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
            cell = Cell(val, length)
            is_numeric = type(val) is float or (type(val) is int)
            align = Align.right if is_numeric else Align.left
            cell.align(align)
            return cell

        return list(map(lambda row: list([get_cell(row[i], self._widths[i]) for i in range(len(row))]), rows))


if __name__ == '__main__':
    n = 1
    print(type(n) is int)
    m = 1.5
    print(type(m) is float or (type(m) is int))
