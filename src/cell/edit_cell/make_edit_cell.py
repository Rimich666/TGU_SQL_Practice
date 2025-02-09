from src.cell.cell import ValueType
from src.cell.edit_cell.date_cell import DateCell
from src.cell.edit_cell.int_cell import IntCell
from src.cell.edit_cell.real_cell import RealCell
from src.cell.edit_cell.text_cell import TextCell


def make_edit_cell(value, width, type_cell):
    if type_cell == ValueType.text:
        return TextCell(value, width)
    if type_cell == ValueType.integer:
        return IntCell(value, width)
    if type_cell == ValueType.date:
        return DateCell(value, width)
    if type_cell == ValueType.real:
        return RealCell(value, width)
