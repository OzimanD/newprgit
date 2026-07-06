# OOP
# Найменування
# Кількість
# Ціна
# Виробник
# Дата_випуску
# Визначити середню вартість товарів і товар мінімальною вартістю.


class Article:
    def __init__(self, name, quantity, price, manufacturer, release_date):
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__manufacturer = manufacturer
        self.__release_date = release_date

    def __str__(self):
        return f"{self.__name}, {self.__quantity}, {self.__manufacturer}, {self.__release_date}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def number(self):
        return self.__quantity

    @number.setter
    def number(self, number):
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    @property
    def release_date(self):
        return self.__release_date

    @release_date.setter
    def release_date(self, release_date):
        self.__release_date = release_date


a1 = Article("Ноутбук", 100, 2000, "Samsung", "11.03.2020")
a2 = Article("Телефон", 30, 19300, "Iphone", "27.10.2026")
a3 = Article("Монітор", 267, 1770, "LG", "29.07.1874")
a4 = Article("Клавіатура", 36, 237, "Atech", "18.03.1999")
a5 = Article("Мишка", 47, 175, "Logi", "01.11.1289")

Article = [a1, a2, a3, a4, a5]
print(Article)


def show_results(articles):
    total_price = 0
    min_article = articles[0]

    for article in articles:
        total_price += article.price

        if article.price < min_article.price:
            min_article = article

    average_price = total_price / len(articles)

    print("Середня вартість товарів:", average_price)
    print("Товар з мінімальною вартістю:", min_article.name)
    print("Його ціна:", min_article.price)


show_results(Article)
