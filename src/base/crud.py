import json
from functools import reduce
from pathlib import Path

from src.base.database import get_connection, exec_script, get_one, get_all
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
    RETURNING id;
    """
    return get_one(query)


def select_all(table):
    fields = get_fields(table, True)[2:]
    pk = [field[0] for field in fields if field[2] == 1][0]
    fields_name = [field[0] for field in fields]
    columns = {field: True for field in fields_name}
    where = {fields_name[0]: False}
    return select({
        'table': table,
        'select': columns,
        'where': where
    }), pk


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


def update_book(book_id, title=None, author=None, published_year=None, genre=None):
    """
    Обновляет данные книги по ее ID.
    """
    conn = get_connection()
    cursor = conn.cursor()
    updates = []
    if title:
        updates.append(f"title = '{title}'")
    if author:
        updates.append(f"author = '{author}'")
    if published_year:
        updates.append(f"published_year = {published_year}")
    if genre:
        updates.append(f"genre = '{genre}'")
    query = f"UPDATE Books SET {', '.join(updates)} WHERE id = {book_id}"
    cursor.execute(query)
    conn.commit()
    conn.close()


def delete_book(book_id):
    """
    Удаляет книгу по ID.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    print(select({'table': 'users'}))
