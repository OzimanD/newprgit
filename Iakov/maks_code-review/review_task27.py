# Завдання 9: Копія, яка не копія (Тема: Посилання в пам'яті)
# Сценарій: Ми хочемо зробити резервну копію списку покупок,
# а потім додати новий товар лише в оригінальний список.
# Але товар чомусь додається в обидва списки.
original_basket = ["молоко", "хліб"]
backup_basket = original_basket.copy()

original_basket.append("кава")

print("Оригінал:", original_basket) # ['молоко', 'хліб', 'кава']
print("Бэкап:", backup_basket)     # Теж ['молоко', 'хліб', 'кава']!

# Підказка: Оператор = не копіює сам об'єкт,
# він лише створює нове посилання на той самий список у пам'яті.
# Як зробити чесну копію списку?

'''++Good job, would do (and did) the same way. The only other alternative I see is:
original_basket = ["молоко", "хліб"]
backup_basket = original_basket[:]

original_basket.append("кава")

print("Оригінал:", original_basket)
print("Бэкап:", backup_basket)
'''