from src.base.database import initialize_database, get_connection
from src.cell.edit_cell.edit_cell import Mode
from src.screen.actions_menu import ActionsMenu
from src.screen.insert import Insert
from src.screen.tables_menu import TablesMenu
from src.terminal.terminal import Terminal
from wait_key import Key


class App(object):
    def __init__(self):
        self.actions_menu = ActionsMenu(
            [
                ('Добавить', self._insert),
                ('Посмотреть', self._select),
                ('Изменить', self._update),
                ('Удалить', self._delete),
                ('Назад', self.pop_screen)
            ]
        )
        self.tables_menu = TablesMenu(
            self.enter_table,
            [
                ('Выход', self._stop)
            ]
        )
        self.screens = []
        self.conn = get_connection()
        self._is_run = True
        self._table = None
        self.check_key = Key.control
        self._mode = Mode.view
        self._callback = None
        initialize_database(self.conn)

    def on_press(self, key):
        if key == Key.enter:
            res = self.screens[0].enter()
            if res:
                cell = res
                self._mode = cell.mode
                if cell.mode == Mode.edit:
                    self._callback = cell.on_press
                    self.check_key = cell.check_keys
        else:
            print(key)
            getattr(self.screens[0], key)()

    def _stop(self):
        self._is_run = False

    def start(self):
        self.add_screen(self.tables_menu)
        while self._is_run:
            Terminal.clear()
            self.screens[0].print()
            key = Key.wait(self.check_key)
            if key == Key.close:
                self._is_run = False
            elif self._mode == Mode.view:
                self.on_press(key)
            elif key and self._mode == Mode.edit:
                if self._callback(key):
                    self._mode = Mode.view
                    self.check_key = Key.control

    def _insert(self):
        self.add_screen(Insert(
            self._table,
            [
                ('Назад', self.pop_screen)
            ]))

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

    def enter_table(self, name):
        self._table = name
        self.add_screen(self.actions_menu)
