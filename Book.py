class Book:
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author: str = author

    def get_name():
        return self.__name

    def get_author():
        return self.__author

name = input()
author = input()

book = Book(name, author)

print(book.get_author(), " ", book.get_name())
