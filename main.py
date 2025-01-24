import os
import sys
from signal import signal, SIGINT

import keyboard

from src.database import initialize_database

from src.screen.main_menu import MainMenu
from src.terminal.cursor import Cursor
from src.terminal.terminal import Terminal


def handler(signal_received, frame):
    Terminal.clear()
    Cursor.show()
    exit(0)


def main():
    is_pycharm = os.getenv("PYCHARM_HOSTED") is not None

    def select_operation(index):
        pass

    main_menu = MainMenu()

    if is_pycharm:
        print('Не надо запускать меня из Pycharm. У Вас есть эмулятор терминала, запуститесь от туда.')
        exit(1)
    Cursor.hide()
    initialize_database()
    screens = [main_menu]

    def on_press(key):
        if key.name == 'down':
            screens[0].down()
        if key.name == 'up':
            screens[0].up()

    keyboard.on_press(on_press)
    Terminal.clear()
    sys.stdout.flush()

    i = 0
    while True:
        i += 1
        Terminal.to_begin()
        screens[0].print()


if __name__ == '__main__':

    signal(SIGINT, handler)
    main()
