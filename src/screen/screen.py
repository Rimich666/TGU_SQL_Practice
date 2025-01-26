import sys

from src.terminal.background import Back
from src.terminal.text import Text


class Screen(object):
    def __init__(self, on_enter=None):
        self.current_line = 0
        self.on_enter = on_enter
        self.title = ''
        self.lines = []

    def print(self):
        sys.stdout.write(Back.default + Text.default)
        print(f'{self.title}\n')
        for i, line in enumerate(self.lines):
            if i == self.current_line:
                sys.stdout.write(Back.white + Text.black)
            else:
                sys.stdout.write(Back.default + Text.default)
            print(i, line)

    def down(self):
        self.current_line = (self.current_line + 1) % len(self.lines)

    def up(self):
        self.current_line = (self.current_line - 1) % len(self.lines)

    def enter(self):
        pass


if __name__ == '__main__':
    print(-1 % 6)
