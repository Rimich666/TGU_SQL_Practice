from src.cell.cell import Cell, Mode, CellParam
from src.terminal.background import Back
from src.terminal.text import Text


class ActionCell(Cell):
    def __init__(self, value, on_action=None):
        super().__init__(value)
        self._on_action = on_action
        self.mode = Mode.action
        self._not_active = CellParam(Text.cyan, Back.black, Text.thin)
        self._active = CellParam(Text.cyan, Back.white, Text.bold)
        self._param = self._not_active

    def on_enter(self):
        self._on_action()
