from Laptop import *


class AppleLaptop(Laptop):
    def __init__(self, brand, screen_size, price, ram, model, chip):
        super().__init__(brand, screen_size, price, ram)

        self.__model = self.__validate_model(model)
        self.__chip = self.__validate_chip(chip)

    @staticmethod
    def __validate_model(value):
        if not isinstance(value, str):
            raise TypeError("Модель повинна бути рядком")

        value = value.strip()

        if len(value) < 2:
            raise ValueError("Назва моделі повинна містити не менше 2 символів")

        return value

    @property
    def model(self):
        return self.__model

    @staticmethod
    def __validate_chip(value):
        if not isinstance(value, str):
            raise TypeError("Назва процесора повинна бути рядком")

        value = value.strip()

        if len(value) < 2:
            raise ValueError("Назва процесора повинна містити не менше 2 символів")

        return value

    @property
    def chip(self):
        return self.__chip

    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Модель: {self.model}\n"
            f"Процесор: {self.chip}"
        )
