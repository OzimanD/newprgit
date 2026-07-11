from Methods import *
def find_max_product(products):
    maxProduct = products[0]

    for product in products:
        if product.get_quantity() > maxProduct.get_quantity():
            maxProduct = product

    print(maxProduct)