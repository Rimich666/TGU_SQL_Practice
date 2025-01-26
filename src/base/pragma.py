from src.base.database import get_connection


def get_tables():
    """
    Возвращает список всех таблиц.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_schema WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return tables
