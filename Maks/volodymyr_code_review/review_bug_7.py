#  Загублена сума (Тема: Область видимості / Scope)
#
# Сценарій: Функція має рахувати загальну вартість товарів у кошику, додаючи до неї фіксовану вартість доставки.
#  Але інтерпретатор видає помилку UnboundLocalError.

# Підказка: Python вважає змінну total_price всередині функції локальною,
# бо ти намагаєшся її там перезаписати. Як сказати функції, що треба використовувати глобальну змінну?
# (Або як змінити архітектуру функції, щоб уникнути global?)


total_price = 0
shipping_cost = 50

def add_to_cart(item_price):
    # Додаємо ціну товару та доставку до загальної суми
    return total_price + item_price + shipping_cost

# Сценарій покупки
print(add_to_cart(150))


"""
good solution. you could also write it like and save total price in new variable to return it later



total_price = 0
shipping_cost = 50

def add_to_cart(item_price):
    # Додаємо ціну товару та доставку до загальної суми
    total_price = item_price + shipping_cost
    return total_price

# Сценарій покупки
print(add_to_cart(150))



"""