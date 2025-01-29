import os
import sys
from signal import signal, SIGINT, SIGTSTP
from src.app.app import App
from src.terminal.background import Back
from src.terminal.cursor import Cursor
from src.terminal.terminal import Terminal
from src.terminal.text import Text


def set_default():
    Terminal.clear()
    Cursor.show()
    sys.stdout.write(Back.default + Text.default)


def handler(signal_received, frame):
    set_default()
    exit(0)


def main():
    is_pycharm = os.getenv("PYCHARM_HOSTED") is not None
    if is_pycharm:
        print('Не надо запускать меня из Pycharm. У Вас есть эмулятор терминала, запуститесь от туда.')
        exit(1)
    signal(SIGINT, handler)
    signal(SIGTSTP, handler)
    Cursor.hide()
    app = App()
    app.start()
    set_default()


if __name__ == '__main__':

    main()
