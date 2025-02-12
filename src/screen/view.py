from src.screen.screen import Screen


class View(Screen):
    def __init__(self, rows, actions=None):
        super().__init__(actions=actions)
        self._fields = rows
        self.set_fields()
