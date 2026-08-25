class Book:
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author: str = author

name = input()
author = input()

book = Book(name, author)
