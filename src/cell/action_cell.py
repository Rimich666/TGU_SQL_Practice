from src.cell.cell import Cell


class ActionCell(Cell):
    def __init__(self, value, on_action=None):
        super().__init__(value)
        self._on_action = on_action

    def enter(self):
        self._on_action()
