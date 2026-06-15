# 2. Розпакування багажу
# Умова: Є кортеж із трьох елементів, що описує товар: ("Ноутбук", 25000, "В наявності").
# Розпакуй ці значення в три окремі змінні (name, price, status) і виведи кожну з них.
# Підказка: Використовуй множинне присвоювання: name, price, status = мій_кортеж.

item = ("Ноутбук", 25000, "В наявності")
def unpack_tuple(my_tuple: tuple)->None:
    print(item)
    name, price, quantity = item
    print(name, price, quantity, sep=' || ')
unpack_tuple(item)