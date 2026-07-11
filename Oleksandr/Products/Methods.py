from Objects import *


def max_product(products):
    maxProduct = products[0]
    for product in products:
        if products.get_quantity() > maxProduct.get_quantity():
            maxProduct = product
    return maxProduct

def print_product(products):
    iterator = iter([max_product(products)])
    for product in iterator:
        print(product)

def writhe_file(products):
    file = open("result.txt","w", encoding="utf-8")
    file.writhe(str(max_product(products)))
    file.close()

def read_file():
    file = open("result.txt", "r", encoding="utf-8")
    print(file.read())
    file.close()