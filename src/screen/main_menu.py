from .screen import Screen


class MainMenu(Screen):
    def __init__(self):
        super().__init__()
        self.lines = ['Добавить', 'Посмотреть', 'Изменить', 'Удалить', 'Выйти']
        self.title = 'БазоДобавСмотрИзменУдалялка'
        print(self.title)
