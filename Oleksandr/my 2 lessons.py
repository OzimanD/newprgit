# Автор
# Кількість сторінок
# Тираж
# Рік видання
# Вивести дані про книги, у яких кількість сторінок більша за 150

class Book:
    def __init__(self, number_of_pages, circulation, year_of_publication):
        self.__number_of_pages = number_of_pages
        self.__circulation = circulation
        self.__year_of_publication = year_of_publication
    def __str__(self):
        return f"{self number_of_pages}, {self.circulation}, {self.year_of_publication}"

a1 = Book(number_of_pages=346, circulation=6000, year_of_publication=2028)
a2 = Book(number_of_pages=346, circulation=6000, year_of_publication=2028)


