from functools import reduce

from src.base.database import get_one, get_all


def get_tables():
    """
    Возвращает список всех таблиц.
    """
    query = """
    SELECT name 
    FROM sqlite_master 
    WHERE type='table' AND NOT substr(name, 1, 6) = 'sqlite';
    """

    return get_all(query)


def get_fields(table, with_pk=True):
    """
    Возвращает поля таблицы.
    """
    query = f"""
        SELECT NOT sql LIKE "%INTEGER PRIMARY KEY AUTOINCREMENT%" AS no_auto 
        FROM sqlite_master 
        WHERE name='{table}';
    """
    print(query)
    no_auto = get_one(query)
    query = f"""
        SELECT name, type, pk
        FROM PRAGMA_table_info('{table}');
    """
    print(query)
    info = get_all(query)

    cond = with_pk + no_auto + 1
    fields = list(filter(lambda row: int(row[2]) < cond, info))
    pk = list(filter(lambda row: int(row[2]) == 1, info))[0][0]

    fields.insert(0, ('name', 'type', 'pk'))
    width = tuple(map(max, reduce(append, fields, [[] for _ in fields[0]])))
    fields.insert(1, width)
    return fields, pk


def get_foreign_keys(table):
    print('get_foreign_keys')
    query = f"""
    SELECT "table", "from", "to" 
    FROM PRAGMA_foreign_key_list('{table}');
    """
    res = get_all(query)
    keys = {row[1]: {'table': row[0], 'to': row[2]} for row in get_all(query)} if res else {}
    return keys


def append(acc, cur):
    for index in range(len(cur)):
        acc[index].append(len(str(cur[index])))
    return acc


if __name__ == '__main__':
    print(get_foreign_keys('user_lists'))
