OOP. 3
Найменування
Кількість
Ціна
Виробник
Дата_випуску
Визначити середню вартість товарів і товар мінімальною вартістю.


class Article:
    def __init__(self, name,number,price,producer,release_date):
        self.__name = name
        self.__number = number
        self.__price = price
        self.__producer = producer
        self.__release_date = release_date

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self,number):
        self.__number = number

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,price):
        self.__price = price

    @property
    def producer(self):
        return self.__producer
    @producer.setter
    def producer(self,producer):
        self.__producer = producer


