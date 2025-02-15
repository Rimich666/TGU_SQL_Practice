from .screen import Screen


class ActionsMenu(Screen):
    def __init__(self, actions):
        super().__init__(actions=actions)
        self._table = ''
        self._title = f'Выберите действие для таблицы'
        super().set_actions()

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, table):
        self._table = table
        self._title = f'Выберите действие для таблицы "{self._table}"'
