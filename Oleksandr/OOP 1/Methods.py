from Objects import *


def count_ram_more_10(products):
    count = 0

    for product in products:
        if product.get_ram() > 10:
            count += 1

    return count


def print_product(products):
    iterator = iter(products)

    for product in iterator:
        if product.get_ram() > 10:
            print(product)


def write_file(products):
    file = open("result.txt", "w", encoding="utf-8")

    for product in products:
        if product.get_ram() > 10:
            file.write(str(product) + "\n")

    file.write("Кількість комп'ютерів з RAM більше 10 ГБ: ")
    file.write(str(count_ram_more_10(products)))

    file.close()


def read_file():
    file = open("result.txt", "r", encoding="utf-8")
    print(file.read())
    file.close()