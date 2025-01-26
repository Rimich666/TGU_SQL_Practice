from src.base.pragma import get_tables
from src.screen.screen import Screen


class TablesMenu(Screen):
    def __init__(self, on_enter):
        super().__init__(on_enter)
        self.lines = [row[0] for row in get_tables()]
