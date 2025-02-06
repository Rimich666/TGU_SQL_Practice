import sys


class Cursor(object):
    invisible = "\033[?25l"
    visible = "\033[?25h"

    @staticmethod
    def hide():
        sys.stdout.write(Cursor.invisible)

    @staticmethod
    def show():
        sys.stdout.write(Cursor.visible)


if __name__ == "__main__":
    Cursor.hide()
    Cursor.show()
