from src.cell.Align import Align
from src.cell.cell import Cell
from src.cell.choice_cell import ChoiceCell
from src.cell.value_type import ValueType
from src.cell.edit_cell.make_edit_cell import make_edit_cell
from src.screen.screen import Screen


class Update(Screen):
    def __init__(self, table, props, actions, on_choice):
        super().__init__(actions=actions, on_enter=on_choice)
        self._table = table
        self._title = f'Изменение записи в таблице "{self._table}"'
        self._values = props['values']
        self._pk, self._pk_val = props['pk']
        self._create_fields(props)
        self.set_fields()

    def _create_fields(self, props):
        headers = ('name', 'type', 'value')
        width = (
            max([len(str(col)) for col in props['columns']] + [len(headers[0])]),
            max([len(str(col)) for col in props['types']] + [len(headers[1])]),
            max([len(str(col)) for col in props['values']] + [len(headers[2])]),
        )
        rows = [(props['columns'][i], props['types'][i], props['values'][i]) for i in range(len(props['columns']))]
        self._fields = [headers, width] + rows

    def make_lines(self, rows):
        def get_cell(item):
            index, line = item
            type_val = line[1].value
            val = self._fields[index + 2][2]
            width = self._fields[1][2]
            name = self._fields[index + 2][0]
            fk = self._fk.get(name, None)
            if fk is None and name != self._pk:
                return line + [make_edit_cell(val, width, ValueType.map[type_val])]
            cell = Cell(val, width) if name == self._pk else ChoiceCell((val, fk, name), width)
            cell.align = Align.by_type(ValueType.map[line[1].value])
            return line + [cell]

        lines = list(map(lambda item: get_cell(item), enumerate(super().make_lines([row[:-1] for row in rows]))))
        return lines

    def get_values(self):
        values = [(item[0].value, item[2].value) for item in self._lines[:len(self._fields) - 2]]
        fields = {row[1]: row[2] for row in filter(
            lambda item: item[2] != self._values[item[0]], [(i, *v) for i, v in enumerate(values)])}
        return {
            'table': self._table,
            'fields': fields,
            'where': {
                'pk': self._pk,
                'value': self._pk_val
            }
        }
