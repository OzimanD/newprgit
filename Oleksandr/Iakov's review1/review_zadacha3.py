guests = ["Оля", "Іван", "Марія", "Іван", "Петро"]

new_guest = input("Введіть ім'я нового гостя: ")

guests.append(new_guest)

print("Список гостей:", guests)
print("Загальна кількість елементів:", len(guests))

"Nice code. But you could do without append() just using insert()"

guests = ["Оля", "Іван", "Марія", "Іван", "Петро"]

new_guest = input("Введіть ім'я нового гостя: ")

guests.insert(len(guests), new_guest)

print("Список гостей:", guests)
print("Загальна кількість елементів:", len(guests))