from src.screen.screen import Screen


class View(Screen):
    def __init__(self, rows, actions):
        super().__init__()
        self._fields = rows
        self._headers = self._fields[0]
        self._widths = self._fields[1]
        self._actions = actions
        self._lines = self.make_lines(self._fields[2:])
        super().set_actions()
        self.make_header()
