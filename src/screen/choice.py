from src.base.crud import select_all
from src.screen.screen import Screen


class Choice(Screen):
    def __init__(self, table, on_enter=None, actions=None, props=None):
        super().__init__(on_enter, actions)
        self._table = table
        rows, _, self._pk, self._types = select_all(self._table)
        self._fields = list(rows)
        field_from = props.get('from', False)
        title_field = f''' в поле "{field_from}"''' if field_from else ''
        self._title = f'''Выбор записи для {props['action']}{title_field} таблицы "{props['table']}"'''
        self.set_fields()

    def reinit(self):
        rows = select_all(self._table)[0]
        self._lines = self.make_lines(list(rows)[2:])
        self.set_actions()

    @property
    def pk(self):
        cell = self._lines[self.current_line][self._headers.index(self._pk)]
        return self._pk, cell.value

    @property
    def values(self):
        return [cell.value for cell in self._lines[self.current_line]]

    @property
    def columns(self):
        return self._fields[0]

    @property
    def types(self):
        return self._types
