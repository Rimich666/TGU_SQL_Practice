from .screen import Screen


class ActionsMenu(Screen):
    def __init__(self, on_enter):
        super().__init__(on_enter)
        self.lines = ['Добавить', 'Посмотреть', 'Изменить', 'Удалить', 'Выйти']
        self.title = 'БазоДобавСмотрИзменУдалялка'
        print(self.title)

    def enter(self):
        self.on_enter(self.current_line)
