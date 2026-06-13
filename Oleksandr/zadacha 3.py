guests = ["Оля", "Іван", "Марія", "Іван", "Петро"]

new_guest = input("Введіть ім'я нового гостя: ")

guests.append(new_guest)

print("Список гостей:", guests)
print("Загальна кількість елементів:", len(guests))