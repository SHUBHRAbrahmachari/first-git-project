from Book import Book

class Library:
    def __init__(self, books: list[Book] | None = None):
        self.__books: list[Book] = books if books is not None else []

    def add_book(book: Book):
        self.__books.append(book)
