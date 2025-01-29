from src.base.database import initialize_database, get_connection
from src.screen.actions_menu import ActionsMenu
from src.screen.insert import Insert
from src.screen.tables_menu import TablesMenu
from src.terminal.terminal import Terminal
from wait_key import Key


class App(object):
    def __init__(self):
        self.actions_menu = ActionsMenu(self.enter_action)
        self.tables_menu = TablesMenu(self.enter_table)
        self.screens = []
        self.conn = get_connection()
        self._is_run = True
        self._table = None
        self._actions = [self._insert, self._select, self._update, self._delete, self.pop_screen]
        initialize_database(self.conn)

    def on_press(self, key):
        if key.name == 'down':
            self.screens[0].down()
        if key.name == 'up':
            self.screens[0].up()
        if key.name == 'left':
            self.screens[0].left()
        if key.name == 'right':
            self.screens[0].right()
        if key.name == 'enter':
            self.screens[0].enter()

    def _stop(self):
        self._is_run = False

    def start(self):
        self.add_screen(self.tables_menu)
        while self._is_run:
            Terminal.clear()
            self.screens[0].print()
            key = Key.wait()
            if key == Key.down:
                self.screens[0].down()
            elif key == Key.up:
                self.screens[0].up()
            elif key == Key.left:
                self.screens[0].left()
            elif key == Key.right:
                self.screens[0].right()
            elif key == Key.enter:
                self.screens[0].enter()
            elif key == Key.close:
                self._is_run = False

    def _insert(self):
        self.add_screen(Insert(self._table))
        pass

    def _select(self):
        pass

    def _update(self):
        pass

    def _delete(self):
        pass

    def add_screen(self, screen):
        Terminal.clear()
        self.screens.insert(0, screen)

    def pop_screen(self):
        self.screens.pop(0)

    def enter_action(self, index):
        if self._table is None:
            self.pop_screen()
            return
        self._actions[index]()

    def enter_table(self, name):
        if name == 'Выход':
            self._stop()
            return
        self._table = name
        self.add_screen(self.actions_menu)
