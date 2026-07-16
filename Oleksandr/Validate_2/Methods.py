def find_most_expensive(products):
    most_expensive = products[0]

    for product in products:
        if product.price > most_expensive.price:
            most_expensive = product

    return most_expensive


def print_most_expensive(products):
    most_expensive = find_most_expensive(products)

    print(most_expensive)


def write_file(products):
    most_expensive = find_most_expensive(products)

    file = open("products.txt", "w", encoding="utf-8")

    file.write("Найдорожчий товар на складі:\n")
    file.write(str(most_expensive))

    file.close()


def read_file():
    file = open("products.txt", "r", encoding="utf-8")

    print(file.read())

    file.close()