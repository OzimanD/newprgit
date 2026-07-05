# Автор
# Кількість сторінок
# Тираж
# Рік видання
# Вивести дані про книги, у яких кількість сторінок більша за 150
from Volodymyr.myclass import print_number


class Book:
    def __init__(self, autor, number_of_pages, circulation, year_of_publication):
        self.__autor = autor
        self.__number_of_pages = number_of_pages
        self.__circulation = circulation
        self.__year_of_publication = year_of_publication

    @property
    def autor(self):
        return self.__autor
    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def number_of_pages(self, number_of_pages):
        return self.__number_of_pages
    @number_of_pages.setter
    def number_of_pages(self, number_of_pages):
        if number_of_pages > 150:
            self.__number_of_pages = number_of_pages
        else:
            print("Кількість сторінок має бути більшою за 150")

    @property
    def circulation(self, circulation):
        return self.__circulation
    @circulation.setter
    def circulation(self, circulation):
        if circulation >= 0:
            self.__circulation = circulation
        else:
            print ("Тираж не може бути від'ємним")

    @property
    def year_of_publication(self, year_of_publication):
        return self.__year_of_publication
    @year_of_publication.setter
    def year_of_publication(self, year_of_publication):
        if year_of_publication >= 0:
            self.__year_of_publication = year_of_publication
        else:
            print ("Рік видання має бути більше за 0")

    def __str__(self):
        return f"{self.number_of_pages}, {self.circulation}, {self.year_of_publication}"



a1 = Book("Rid",  6000,  2028)
a2 = Book("Doil",  3000,  2030)
a3 = Book( "King", 2000, 2045)
a4 = Book("Chaldini",   34, 2052)
a5 = Book("Puaro", 39, 2056)

books = [a1, a2, a3, a4, a5]
print(books)

def more_than_150_pages(books):
    count = []

    for book in books:
        if book.number_of_pages > 150:
            result.append(book)

    return count

result_list = more_than_150_pages(books)

for book in result_list:
    print(book)
