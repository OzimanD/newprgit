class Product:
    def __init__(self, name, quantity, price,year, manufacturer):
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__year = year
        self.__manufacturer = manufacturer

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_manufacturer(self):
        return self.__manufacturer

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year










