from src.base.pragma import get_tables
from src.screen.screen import Screen


class TablesMenu(Screen):
    def __init__(self, on_enter):
        super().__init__(on_enter)
        self._title = "Выберите таблицу"
        self.lines = get_tables()
        self.lines.append(('Выход',))

    def enter(self):
        self.on_enter(self.lines[self.current_line][self.current_column])
