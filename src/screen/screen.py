import os
import sys

from src.cell.action_cell import ActionCell
from src.cell.cell import Cell, Align
from src.cell.edit_cell.edit_cell import EditCell
from src.cell.edit_cell.text_cell import TextCell
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

    def set_fields(self):
        self._headers = self._fields[0]
        self._widths = self._fields[1]
        self._lines = self.make_lines(self._fields[2:])
        self.set_actions()
        self.make_header()

    def set_actions(self):
        if self._actions is not None:
            for action in self._actions:
                self._lines.append([ActionCell(*action)])
        self._lines[self.current_line][self.current_column].active(True)

    def print(self):
        sys.stdout.write(Back.default + Text.default)
        if self._title:
            sys.stdout.write(Back.default + Text.title + self._title + '\n\n')
        if self._header:
            self.print_header()
        for i, line in enumerate(self._lines):
            len_i = len(str(i))
            width_i = len(str(len(self._fields) - 1))
            sys.stdout.write(Back.default + Text.default + f'{(width_i - len_i) * " "}{i}')
            for cell in line:
                sys.stdout.write(Back.default + Text.line + ' | ')
                cell.print()

            sys.stdout.write('\n')
        sys.stdout.write(Back.default + Text.default)

    def print_header(self):
        len_line = sum([len(head) + 3 for head in self._header])
        sys.stdout.write(Back.default + Text.line + len_line * '-' + '\n')
        sys.stdout.write(Back.head + Text.head + f'{self._header[0]}')
        for head in self._header[1:]:
            sys.stdout.write(Back.default + Text.line + ' | ')
            sys.stdout.write(Back.head + Text.head + f'{head}')
        sys.stdout.write('\n')
        sys.stdout.write(Back.default + Text.line + len_line * '-' + '\n')

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

    def delete(self):
        cell = self._lines[self.current_line][self.current_column]
        if isinstance(cell, EditCell):
            cell.clear()

    def enter(self):
        cell = self._lines[self.current_line][self.current_column]
        if isinstance(cell, ActionCell):
            cell.on_enter()
        elif isinstance(cell, EditCell):
            cell.on_enter()
            return cell
        else:
            if self.on_enter:
                self.on_enter(cell.on_enter())

    def make_header(self):
        def get_head(val, length):
            print('length =', length)
            len_val = len(str(val))
            before = (length - len_val) // 2
            after = length - len_val - before
            return f"{before * ' '}{val}{after * ' '}"

        if self._fields:
            headers = [get_head(self._headers[i], self._widths[i]) for i in range(len(self._widths))]
            headers.insert(0, get_head('№', len(str(len(self._fields) - 1))))
            self._header = headers
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
