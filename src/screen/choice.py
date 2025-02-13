from src.screen.screen import Screen


class Choice(Screen):
    def __init__(self, rows, pk, on_enter=None, actions=None):
        super().__init__(on_enter, actions)
        self._pk = pk
        self._fields = rows,
        self.set_fields()

    @property
    def pk(self):
        cell = self._lines[self.current_line][self._headers.index(self._pk)]
        return cell.value

    @property
    def values(self):
        return [cell.value for cell in self._lines[self.current_line]]
