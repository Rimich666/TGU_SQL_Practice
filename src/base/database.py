import os
import sqlite3  # SQLite входит в стандартную библиотеку Python
from pathlib import Path


def log(text):
    path = Path(__file__).parents[2].joinpath('data').joinpath("log.txt")
    with open(path, 'a') as file:
        file.write(text + '\n')


def get_connection():
    """Создает соединение с базой данных."""
    dir_path = Path(__file__).parents[2].joinpath('data')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    path = Path(dir_path).joinpath('base.db')
    return sqlite3.connect(path)


def exec_script(conn, query):
    cursor = conn.cursor()
    cursor.executescript(query)
    conn.commit()
    conn.close()


def initialize_database(conn):
    """
    Создает таблицы в базе данных, если они еще не существуют.
    Эта функция запускается один раз при старте приложения.
    """
    with open(Path(__file__).parents[0].joinpath('sql', 'create_tables.sql'), 'r') as f:
        query = f.read()
    exec_script(conn, query)


def clean_after_yourself(conn):
    with open(Path(__file__).parents[0].joinpath('sql', 'drop_tables.sql'), 'r') as f:
        query = f.read()
        exec_script(conn, query)


def get_one(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    res = cursor.fetchone()
    conn.commit()
    conn.close()
    return res[0] if res else None


def get_all(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    conn.close()
    return res


def execute(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    initialize_database(get_connection())
