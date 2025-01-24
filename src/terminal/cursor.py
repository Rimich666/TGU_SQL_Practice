import sys


class Cursor(object):
    @staticmethod
    def hide():
        sys.stdout.write("\033[?25l")

    @staticmethod
    def show():
        sys.stdout.write("\033[?25h")
