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


def get_fields(table):
    """
    Возвращает поля таблицы.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT name, type, pk
        FROM PRAGMA_table_info('{table}');
    """)
    tables = cursor.fetchall()
    conn.close()
    tables.insert(0, ('name', 'type', 'pk'))
    width = tuple(map(max, reduce(append, tables, [[] for _ in tables[0]])))
    tables.insert(1, width)
    return tables


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

    fields = get_fields('users')
    header = make_header(fields)
    # lines = make_lines(fields[2:], fields[1])
    # print(lines)
