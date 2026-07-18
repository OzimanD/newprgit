from AppleLaptop import *


def find_largest_screen(laptops):
    result = laptops[0]

    for laptop in laptops:
        if laptop.screen_size > result.screen_size:
            result = laptop

    return result


def find_smallest_screen(laptops):
    result = laptops[0]

    for laptop in laptops:
        if laptop.screen_size < result.screen_size:
            result = laptop

    return result


def find_cheapest(laptops):
    result = laptops[0]

    for laptop in laptops:
        if laptop.price < result.price:
            result = laptop

    return result


def find_most_expensive(laptops):
    result = laptops[0]

    for laptop in laptops:
        if laptop.price > result.price:
            result = laptop

    return result


def find_largest_ram(laptops):
    result = laptops[0]

    for laptop in laptops:
        if laptop.ram > result.ram:
            result = laptop

    return result


def find_smallest_ram(laptops):
    result = laptops[0]

    for laptop in laptops:
        if laptop.ram < result.ram:
            result = laptop

    return result


def analyze_laptops(laptops):
    results = [
        ("Ноутбук з найбільшим екраном", find_largest_screen(laptops)),
        ("Ноутбук з найменшим екраном", find_smallest_screen(laptops)),
        ("Найдешевший ноутбук", find_cheapest(laptops)),
        ("Найдорожчий ноутбук", find_most_expensive(laptops)),
        ("Ноутбук з найбільшим об'ємом RAM", find_largest_ram(laptops)),
        ("Ноутбук з найменшим об'ємом RAM", find_smallest_ram(laptops))
    ]

    return results


class ResultIterator:
    def __init__(self, results):
        self.__results = results
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.__results):
            raise StopIteration

        result = self.__results[self.__index]
        self.__index += 1

        return result


def print_results(results):
    iterator = ResultIterator(results)

    for title, laptop in iterator:
        print("=" * 50)
        print(title)
        print("=" * 50)
        print(laptop)
        print()


def write_file(results):
    file = open("laptop_results.txt", "w", encoding="utf-8")
    iterator = ResultIterator(results)

    for title, laptop in iterator:
        line = (
            f"{title}|{laptop.brand}|{laptop.screen_size}|"
            f"{laptop.price}|{laptop.ram}|{laptop.model}|{laptop.chip}\n"
        )
        file.write(line)

    file.close()


def read_file():
    restored_results = []
    file = open("laptop_results.txt", "r", encoding="utf-8")

    for line in file:
        data = line.strip().split("|")

        title = data[0]
        brand = data[1]
        screen_size = float(data[2])
        price = float(data[3])
        ram = int(data[4])
        model = data[5]
        chip = data[6]

        laptop = AppleLaptop(brand, screen_size, price, ram, model, chip)
        restored_results.append((title, laptop))

    file.close()

    return restored_results
