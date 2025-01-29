import sys


class Terminal(object):
    @staticmethod
    def to_begin():
        sys.stdout.write("\033[H")

    @staticmethod
    def clear():
        sys.stdout.write("\033[H\033[2J")



