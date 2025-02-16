from src.cell.cell import Mode
from src.cell.Align import Align
from src.cell.edit_cell.edit_cell import EditCell
from wait_key import Key


class BoolCell(EditCell):
    def __init__(self, value, width):
        super().__init__(value if value == 1 else 0, width)
        self.check_keys = Key.check
        self._align = Align.center

    def enter(self):
        self._value = 0 if self._value else 1
        self.mode = Mode.view

    def _text(self, value):
        return super()._text('True') if value else super()._text('False')
