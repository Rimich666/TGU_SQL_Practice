from src.cell.cell import Cell, Mode


class ActionCell(Cell):
    def __init__(self, value, on_action=None):
        super().__init__(value)
        self._on_action = on_action
        self.mode = Mode.action

    def enter(self):
        self._on_action()
