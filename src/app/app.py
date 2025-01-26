import sys
from src.base.database import initialize_database, get_connection
from src.screen.actions_menu import ActionsMenu
from src.screen.tables_menu import TablesMenu
from src.terminal.terminal import Terminal


class App(object):
    def __init__(self):
        self.actions_menu = ActionsMenu(self.enter_action)
        self.tables_menu = TablesMenu(self.enter_table)
        self.screens = [self.actions_menu]
        self.conn = get_connection()
        self._is_run = True
        self._table = None
        self.actions = [self._insert, self._select, self._update, self._delete, self._stop]
        initialize_database(self.conn)

    def on_press(self, key):
        if key.name == 'down':
            self.screens[0].down()
        if key.name == 'up':
            self.screens[0].up()
        if key.name == 'enter':
            self.screens[0].enter()

    def _stop(self):
        self._is_run = False

    def start(self):
        Terminal.clear()
        sys.stdout.flush()
        while True:
            Terminal.to_begin()
            self.screens[0].print()

    def _insert(self):
        pass

    def _select(self):
        pass

    def _update(self):
        pass

    def _delete(self):
        pass

    def enter_action(self):
        pass

    def enter_table(self):
        pass
