'''
list

Видалення невдахи

Умова: Маємо список куплених продуктів. Виявилося, що один товар додали помилково (наприклад, "молоко"). Видали цей конкретний товар зі списку за його назвою.

Підказка: Для видалення елемента за його значенням ідеально підійде метод .remove("назва_товару").
'''
from operator import index

products_list = ["banana", "apple", "orange", "milk"]
products_list.remove("milk")

print(products_list)

# as variant)
for item in products_list:
    if item == "apple":
        a = products_list.pop(products_list.index(item))
        print("remove - ", a, "from 'products_list'")
print(products_list)