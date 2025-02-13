from src.base.crud import select
from src.base.pragma import get_fields
from src.screen.screen import Screen


class Update(Screen):
    def __init__(self, table, pk_value, actions):
        super().__init__(actions=actions)
        self._table = table
        fields = get_fields(table, True)
        columns = {item[0].value: True for item in fields[2:]}
        where = {item[0].value: pk_value for item in fields[2:] if item[2] == 1}

        self.set_fields()
