from src.base.pragma import get_fields
from src.cell.Align import Align
from src.cell.choice_cell import ChoiceCell
from src.cell.value_type import ValueType
from src.cell.edit_cell.make_edit_cell import make_edit_cell
from src.screen.screen import Screen

WIDTH = 25


class Insert(Screen):
    def __init__(self, table, actions, on_choice):
        super().__init__(actions=actions, on_enter=on_choice)
        self._table = table
        self._title = f'Добавление записи в таблицу "{self._table}"'
        self._fields, self._pk = get_fields(table, False)
        self.set_fields()

    def make_header(self):
        super().make_header()
        self._header += [f"{' ' * 10}value{' ' * 10}"]

    def make_lines(self, rows):
        def get_cell(line):
            name = line[0].value
            fk = self._fk.get(name, None)
            if fk is None:
                return make_edit_cell('', WIDTH, ValueType.map[line[1].value])
            cell = ChoiceCell(('', fk, name), WIDTH)
            cell.align = Align.by_type(ValueType.map[line[1].value])
            return cell

        lines = list(map(lambda line: line + [get_cell(line)], super().make_lines(rows)))
        return lines

    def get_values(self):
        fields = {item[0].value: item[len(self._fields[0])].value for item in self._lines[:len(self._fields) - 2]}
        return {
            'table': self._table,
            'fields': fields,
            'pk': self._pk
        }
