from src.cell.value_type import ValueType


class Align(object):
    left = 1
    center = 2
    right = 0

    @staticmethod
    def by_type(value_type):
        if value_type == ValueType.text:
            return Align.left
        if value_type == ValueType.real:
            return Align.right
        if value_type == ValueType.integer:
            return Align.right
        if value_type == ValueType.date:
            return Align.right
        if value_type == ValueType.bool:
            return Align.center
