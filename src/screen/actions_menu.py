from .screen import Screen


class ActionsMenu(Screen):
    def __init__(self, on_enter):
        super().__init__(on_enter)
        self._lines = [('Добавить',), ('Посмотреть',), ('Изменить',), ('Удалить',), ('Назад',)]
        self._title = 'Выберите действие'

    def enter(self):
        self.on_enter(self.current_line)
