from src.base.pragma import get_tables
from src.cell.action_cell import ActionCell
from src.cell.cell import Cell
from src.screen.screen import Screen


class TablesMenu(Screen):
    def __init__(self, on_enter, actions):
        super().__init__(on_enter, actions)
        self._title = "Выберите таблицу"
        self._lines = [[Cell(tbl[0])] for tbl in get_tables()]
        super().set_actions()
