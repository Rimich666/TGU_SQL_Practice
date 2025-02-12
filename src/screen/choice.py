from src.screen.screen import Screen


class Choice(Screen):
    def __init__(self, rows, on_enter=None, actions=None):
        super().__init__(on_enter, actions)
        self._fields, self._pk = rows
        self.set_fields()

    def enter(self):
        cell = self._lines[self.current_line][self._headers.index(self._pk)]
        self.on_enter(self._pk, cell.value)
