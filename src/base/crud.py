import json
from pathlib import Path

from src.base.database import get_connection, exec_script


def insert(data):
    """
        Добавляет данные в таблицу.
    """
    # path = Path(__file__).parents[2].joinpath('data').joinpath(f"insert_{data['table']}.json")
    # with open(path, 'w') as file:
    #     file.write(json.dumps(data))
    # with open(path, 'r') as file:
    #     dt = json.loads(file.read())
    query = f"""
    INSERT INTO "{data['table']}"
    ({', '.join([f'"{key}"'for key in data['fields'].keys()])}) 
    VALUES ({', '.join([f'"{val}"' for val in data['fields'].values()])})
    """
    print(query)
    exec_script(get_connection(), query)


def add_book(title, author, published_year, genre):
    """
    Добавляет новую книгу в таблицу Books.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Books (title, author, published_year, genre)
        VALUES (?, ?, ?, ?)
    """, (title, author, published_year, genre))
    conn.commit()
    conn.close()


def get_books():
    """
    Возвращает список всех книг.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    conn.close()
    return books


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
    insert({'table': 'users'})
