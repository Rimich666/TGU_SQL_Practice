
from src.screen.screen import Screen
from src.terminal.text import Text


class View(Screen):
    def __init__(self, props, actions=None):
        super().__init__(actions=actions)
        rows, _, _, title = props
        self._fields = rows
        self._title = f'Просмотр результата запроса: {Text.white}{title.rstrip()}'
        self.set_fields()
