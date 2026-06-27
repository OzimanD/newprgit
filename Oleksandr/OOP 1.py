class Book:
    def __init__(self, author, pages, circulation, year):
        self.__author = author
        self.__pages = pages
        self.__circulation = circulation
        self.__year = year

    @property
    def author(self):
        return self.__author

    @property
    def pages(self):
        return self.__pages

    @property
    def circulation(self):
        return self.__circulation

    @property
    def year(self):
        return self.__year

    def __str__(self):
        return (
            f"Автор: {self.__author}, "
            f"Кількість сторінок: {self.__pages}, "
            f"Тираж: {self.__circulation}, "
            f"Рік видання: {self.__year}"
        )


def get_books_with_pages_more_than(books, page_count):
    result = []

    try:
        if not isinstance(page_count, int):
            raise TypeError("Введіть число, а не символ або рядок")

        for book in books:
            if book.pages > page_count:
                result.append(book)

        return result

    except TypeError as error:
        print(f"Помилка: {error}")
        return result


list_of_books = [
    Book("Тарас Шевченко", 120, 5000, 1840),
    Book("Леся Українка", 210, 3000, 1911),
    Book("Іван Франко", 180, 2500, 1896),
    Book("Микола Гоголь", 95, 4000, 1835),
]

result = get_books_with_pages_more_than(list_of_books, 150)

for book in result:
    print(book)