# Завдання 11: Небезпечний зріз (Тема: Індекси та Slices)
# Сценарій: Ми хочемо розгорнути рядок задом наперед, використовуючи кроки у зрізах,
# але переплутали параметри, і код повертає порожній рядок "".

# text = "Kharkiv"
# print(text)
# # Нам треба отримай "vikrahK"
# reversed_text = text[::-1]
# print(reversed_text)

# Завдання 12: Загадкові відсотки (Тема: Динамічна типізація та input)
# Сценарій: Проста програма для розрахунку чайових (15% від рахунку). Користувач вводить суму,
# але програма вилітає з помилкою.

# bill = int(input("Введіть суму рахунку: "))
# tip = bill * 0.15
# print("Чайові:", tip)

# Завдання 13: Помилка фільтрації (Тема: Генератори списків / List Comprehensions)
# Сценарій: Ми хочемо створити новий список, який містить лише слова довжиною більше 3 символів.
# Програма видає SyntaxError.

# words = ["it", "code", "py", "cool", "am"]
# # Спроба відфільтрувати в один рядок
# long_words = [w for w in words if len(w) > 3]
# print(long_words)


# Завдання 14: Зміна словника на льоту (Тема: Ітерація по словниках)
# Сценарій: Ми хочемо видалити зі словника всіх користувачів, у яких статус inactive. Але Python видає:
# RuntimeError: dictionary changed size during iteration.

# users = {
#     "alex": "active",
#     "john": "inactive",
#     "mary": "active",
#     "olga": "inactive"
# }
#
# copy_users = dict(users)
# print(copy_users)
# for user, status in copy_users.items():
#     if status == "inactive":
#         del users[user]
# print(users)



