from .screen import Screen


class ActionsMenu(Screen):
    def __init__(self, actions):
        super().__init__(actions=actions)
        self._title = 'Выберите действие'
        super().set_actions()
