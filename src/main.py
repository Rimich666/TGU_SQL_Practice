import sys
from signal import signal, SIGINT

import keyboard

from database import initialize_database
from crud import add_book, get_books, update_book, delete_book


def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)


def main():
    initialize_database()
    ctrl = False
    is_exit = False

    def on_press(key):
        nonlocal ctrl
        nonlocal is_exit
        if key.name == 'ctrl':
            ctrl = key.event_type == 'down'
        if key.name == 'c':
            is_exit = key.event_type == 'down' and ctrl

    keyboard.hook(on_press)
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()
    i = 0
    while i < 1:
        i += 1
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        # choice = input("Choose an option: ")

        # if choice == '1':
        #     title = input("Enter title: ")
        #     author = input("Enter author: ")
        #     published_year = int(input("Enter published year: "))
        #     genre = input("Enter genre: ")
        #     add_book(title, author, published_year, genre)
        #
        # elif choice == '2':
        #     books = get_books()
        #     for book in books:
        #         print(book)
        #
        # elif choice == '3':
        #     book_id = int(input("Enter book ID to update: "))
        #     title = input("New title (leave blank to skip): ")
        #     author = input("New author (leave blank to skip): ")
        #     published_year = input("New published year (leave blank to skip): ")
        #     genre = input("New genre (leave blank to skip): ")
        #     update_book(book_id, title or None, author or None, int(published_year) if published_year else None,
        #                 genre or None)
        #
        # elif choice == '4':
        #     book_id = int(input("Enter book ID to delete: "))
        #     delete_book(book_id)
        #
        # elif choice == '5':
        #     break
        #
        # else:
        #     print(choice)
        #     print("Invalid option. Try again.")


if __name__ == '__main__':

    signal(SIGINT, handler)
    main()
