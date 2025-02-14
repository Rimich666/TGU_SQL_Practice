import json
from functools import reduce
from pathlib import Path

from src.base.database import get_connection, get_one, get_all, log, execute
from src.base.pragma import append, get_fields


def to_file(data, action):
    path = Path(__file__).parents[2].joinpath('data').joinpath(f"{action}_{data['table']}.json")
    with open(path, 'w') as file:
        file.write(json.dumps(data))


def from_file(data, action):
    path = Path(__file__).parents[2].joinpath('data').joinpath(f"{action}_{data['table']}.json")
    with open(path, 'r') as file:
        dt = json.loads(file.read())
    return dt


def insert(data):
    """
        Добавляет данные в таблицу.
    """
    query = f"""
    INSERT INTO "{data['table']}"
    ({', '.join([f'"{key}"'for key in data['fields'].keys()])}) 
    VALUES ({', '.join([f'"{val}"' for val in data['fields'].values()])})
    RETURNING {data['pk']};
    """
    return get_one(query)


def select_values(info):
    to_file(info, 'select')
    pass


def select_all(table):
    print(table)
    fields = get_fields(table, True)[0][2:]
    print(fields)
    pk = [field[0] for field in fields if field[2] == 1][0]
    log(str(pk))
    fields_name = [field[0] for field in fields]
    fields_type = [field[1] for field in fields]
    columns = {field: True for field in fields_name}
    where = {fields_name[0]: False}
    return select({
        'table': table,
        'select': columns,
        'where': where
    }), pk, fields_type


def select(data):
    """
        Возвращает выборку из таблицы.
    """
    # to_file(data, 'select')
    # return
    # data = from_file(dt, 'select')
    single_quote = "'"
    is_all = sum(data['select'].values()) == 0
    is_where = sum([not not val for val in data['where'].values()]) > 0
    columns = tuple(f'{key}' for key in filter(
        lambda key: data['select'][key] or is_all, data['select'].keys()))
    where = 'WHERE' + ' AND '.join([f'"{item[0]}" = {single_quote + item[1] + single_quote}' for item in filter(
        lambda item: not not item[1], data['where'].items())]) if is_where else ''
    query = f"""
    SELECT {', '.join([f'"{col}"' for col in columns])} 
    FROM "{data['table']}"
    {where} 
    """
    rows = get_all(query)
    rows.insert(0, columns)
    width = tuple(map(max, reduce(append, rows, [[] for _ in rows[0]])))
    rows.insert(1, width)
    return rows


def update(data):
    # to_file(data, 'update')
    # return True
    # data = from_file(dt, 'update')
    single_quote = "'"
    query_set = ', '.join([f'"{item[0]}" = {single_quote + item[1] + single_quote}' for item in data['fields'].items()])
    where = f'"{data["where"]["pk"]}" = {single_quote + str(data["where"]["value"]) + single_quote}'

    query = f"""
    UPDATE {data['table']} 
    SET {query_set} 
    WHERE {where}
    RETURNING {data["where"]["pk"]};
    """

    return get_one(query)


def delete(data):
    # to_file(data, 'update')
    # return True
    # data = from_file(dt, 'delete')
    single_quote = "'"
    query = f"""
        DELETE FROM {data['table']} 
        WHERE "{data['pk']}" = {single_quote + str(data['val']) + single_quote}
        """
    execute(query)


if __name__ == "__main__":
    print(delete({'table': 'users'}))
