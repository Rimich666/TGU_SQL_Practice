from functools import reduce

from src.base.database import get_connection


def get_tables():
    """
    Возвращает список всех таблиц.
    """
    conn = get_connection()
    cursor = conn.cursor()
    # cursor.execute("SELECT name FROM sqlite_schema WHERE type='table';")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return tables


def get_fields(table, with_pk=True):
    """
    Возвращает поля таблицы.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT NOT sql LIKE "%INTEGER PRIMARY KEY AUTOINCREMENT%" AS no_auto 
        FROM sqlite_master 
        WHERE name='{table}';
    """)
    no_auto = cursor.fetchone()[0]

    cursor.execute(f"""
        SELECT name, type, pk
        FROM PRAGMA_table_info('{table}');
    """)
    cond = with_pk + no_auto + 1
    fields = list(filter(lambda row: int(row[2]) < cond, cursor.fetchall()))

    conn.close()
    fields.insert(0, ('name', 'type', 'pk'))
    width = tuple(map(max, reduce(append, fields, [[] for _ in fields[0]])))
    fields.insert(1, width)
    return fields


def append(acc, cur):
    for index in range(len(cur)):
        acc[index].append(len(str(cur[index])))
    return acc


if __name__ == '__main__':
    def make_header(_fields):
        print(_fields)

        def get_head(val, length):
            len_val = len(str(val))
            before = ((length - len_val) // 2)
            after = length - len_val - before
            return f"{before * ' '}{val}{after * ' '}"

        return ' '.join([get_head(_fields[0][i], _fields[1][i])
                         for i in range(len(_fields[1]))]) if _fields else None


    # def make_lines(rows, widths):
    #     def get_cell(val, length):
    #         is_numeric = type(val) is float or (type(val) is int)
    #         len_val = len(str(val))
    #         before = length - len_val if is_numeric else 0
    #         after = length - len_val - before
    #         return f"{before * ' '}{val}{after * ' '}"
    #
    #     return list(map(lambda row: tuple([get_cell(row[i], widths[i]) for i in range(len(row))]), rows))

    fields = get_fields('audio', True)
    print(fields)
    # header = make_header(fields)
    # lines = make_lines(fields[2:], fields[1])
    # print(lines)
