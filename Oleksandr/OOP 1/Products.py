class Product:
    def __init__(self, name, frequency, ram, dvd_rom, price):
        self.__name = name
        self.__frequency = frequency
        self.__ram = ram
        self.__dvd_rom = dvd_rom
        self.__price = price

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_frequency(self):
        return self.__frequency
    def set_frequency(self, frequency):
        self.__frequency = frequency

    def get_ram(self):
        return self.__ram
    def set_ram(self, ram):
        self.__ram = ram

    def get_dvd_rom(self):
        return self.__dvd_rom
    def set_dvd_rom(self, dvd_rom):
        self.__dvd_rom = dvd_rom

    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return (f"Назва: {self.__name}, Частота: {self.__frequency},"
                f"Обєм ОП: {self.__ram}, Наявність dvd_rom: {self.__dvd_rom},"
                f"вартість: {self.__price}")




