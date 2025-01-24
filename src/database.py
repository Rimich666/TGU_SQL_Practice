import os
import sqlite3  # SQLite входит в стандартную библиотеку Python
from pathlib import Path


def get_connection():
    """Создает соединение с базой данных."""
    dir_path = Path(__file__).parents[1].joinpath('data')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    path = Path(dir_path).joinpath('base.db')
    return sqlite3.connect(path)


def exec_script(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript(query)
    conn.commit()
    conn.close()


def initialize_database():
    """
    Создает таблицы в базе данных, если они еще не существуют.
    Эта функция запускается один раз при старте приложения.
    """
    with open(Path(__file__).parents[0].joinpath('sql', 'create_tables.sql'), 'r') as f:
        query = f.read()
    exec_script(query)


def clean_after_yourself():
    with open(Path(__file__).parents[0].joinpath('sql', 'drop_tables.sql'), 'r') as f:
        query = f.read()
        exec_script(query)


if __name__ == '__main__':
    initialize_database()
    clean_after_yourself()
