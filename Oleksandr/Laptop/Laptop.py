class Laptop:
    def __init__(self, brand, screen_size, price, ram):
        self.__brand = self.__validate_brand(brand)
        self.__screen_size = self.__validate_screen_size(screen_size)
        self.__price = self.__validate_price(price)
        self.__ram = self.__validate_ram(ram)

    @staticmethod
    def __validate_brand(value):
        if not isinstance(value, str):
            raise TypeError("Бренд повинен бути рядком")

        value = value.strip()

        if len(value) < 2:
            raise ValueError("Назва бренду повинна містити не менше 2 символів")

        return value

    @property
    def brand(self):
        return self.__brand

    @staticmethod
    def __validate_screen_size(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Розмір екрана повинен бути числом")

        if value <= 0:
            raise ValueError("Розмір екрана повинен бути більшим за нуль")

        return value

    @property
    def screen_size(self):
        return self.__screen_size

    @staticmethod
    def __validate_price(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Ціна повинна бути числом")

        if value <= 0:
            raise ValueError("Ціна повинна бути більшою за нуль")

        return value

    @property
    def price(self):
        return self.__price

    @staticmethod
    def __validate_ram(value):
        if not isinstance(value, int):
            raise TypeError("Об'єм оперативної пам'яті повинен бути цілим числом")

        if value <= 0:
            raise ValueError("Об'єм оперативної пам'яті повинен бути більшим за нуль")

        return value

    @property
    def ram(self):
        return self.__ram

    def __str__(self):
        return (
            f"Бренд: {self.brand}\n"
            f"Розмір екрана: {self.screen_size} дюймів\n"
            f"Ціна: {self.price} євро\n"
            f"Оперативна пам'ять: {self.ram} ГБ"
        )
