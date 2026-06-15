#5. Забудь старе
# Умова: Створи множину зі своїх поточних завдань на день. Одне завдання ти вже виконав.
# Видали його з множини так, щоб програма не видавала помилку, навіть якщо цього завдання там раптом не виявиться.
# Підказка: Метод .remove() викличе помилку KeyError, якщо елемента немає.
# Тому краще безпечно використовувати метод .discard(елемент).

my_to_do_list = {'swimming', 'chess',  'work', 'music', 'gym', 'reading'}
print(my_to_do_list)
try:
    my_to_do_list.remove('sleeping')
    print(my_to_do_list)  # KeyError: 'sleeping'
except KeyError as e:
    print("Такого не заплановано - ", e)

############################ variant 2

my_to_do_list.discard('sleeping')
print(my_to_do_list)  # ignor error !!!