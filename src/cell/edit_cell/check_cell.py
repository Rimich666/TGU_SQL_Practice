from src.cell.cell import Mode
from src.cell.Align import Align
from src.cell.edit_cell.edit_cell import EditCell
from wait_key import Key


class CheckCell(EditCell):
    def __init__(self):
        super().__init__(False, 6)
        self.check_keys = Key.check
        self._align = Align.center

    def enter(self):
        self._value = not self._value
        self.mode = Mode.view

    def _text(self, value):
        return super()._text('V') if value else super()._text('')
