from datetime import datetime

class Product:
    def __init__(self, name, quantity, price, year, manufacturer):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.year = year
        self.manufacturer = manufacturer

    @staticmethod
    def __validate_name(value):
        if not isinstance(value, str):
            raise TypeError("Назва повинна бути рядком")
        value = value.strip()
        if len(value) < 2:
            raise ValueError("Некоректна назва товару")
        return value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = self.__validate_name(value)

    @staticmethod
    def __validate_quantiti(value):
        if not isinstance(value, int)or value < 0:
            raise ValueError("Кількість - ціле число від 0")
        return value

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, value):
        self.__quantity = self.__validate_quantiti(value)

    @staticmethod
    def __validate_price(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Ціна повинна бути числом")
        if value <= 0:
            raise ValueError("Ціна повинна бути > 0")
        return value

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        self.__price = self.__validate_price(value)

    @staticmethod
    def __validate_year(value):
        current_year = datetime.now().year
        if not isinstance(value,int):
            raise TypeError("Рік повинен бути цілим")
        if value < 1900 or value > current_year:
            raise ValueError("Некоректний рік")
        return value

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, value):
        self.__year = self.__validate_year(value)

    @staticmethod
    def __validate_manufacturer(value):
        if not isinstance(value, str):
            raise TypeError("Виробник повинен бути рядком")
        value = value.strip()
        if len(value) < 2:
            raise ValueError("Некоректний виробник")
        return value

    @property
    def manufacturer(self):
        return self.__manufacturer
    @manufacturer.setter
    def manufacturer(self, value):
        self.__manufacturer = self.__validate_manufacturer(value)

    def __str__(self):
        return (
            f"Назва: {self.name}\n"
            f"Кількість: {self.quantity}\n"
            f"Ціна: {self.price}\n"
            f"Рік виготовлення: {self.year}\n"
            f"Виробник: {self.manufacturer}"
        )

