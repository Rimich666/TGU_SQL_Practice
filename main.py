import os
import sys
from signal import signal, SIGINT
import keyboard
from src.app.app import App
from src.terminal.background import Back
from src.terminal.cursor import Cursor
from src.terminal.terminal import Terminal
from src.terminal.text import Text


def handler(signal_received, frame):
    Terminal.clear()
    Cursor.show()
    sys.stdout.write(Back.default + Text.default)
    exit(0)


def main():
    is_pycharm = os.getenv("PYCHARM_HOSTED") is not None
    if is_pycharm:
        print('Не надо запускать меня из Pycharm. У Вас есть эмулятор терминала, запуститесь от туда.')
        exit(1)
    Cursor.hide()
    app = App()
    keyboard.on_press(lambda key: app.on_press(key))
    app.start()


if __name__ == '__main__':

    signal(SIGINT, handler)
    main()
