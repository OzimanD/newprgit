# Задача 5: Пошук максимального числа
# Користувач спочатку вводить число N (кількість чисел, яку він збирається ввести далі).
# Потім програма N разів запитує нове число.
# Після завершення циклу програма має вивести найбільше число серед усіх введених.
# Використовувати вбудовану функцію max() або списки заборонено.

count_num = int(input("Введіть число N (кількість чисел, які будуть введені далі): "))
def input_date(num:int)->list:
    i = 0
    new_list = []
    while i < count_num:
        new_list.append(int(input("Введіть new число: ")))
        i += 1
    return new_list

def max_number(my_num_list: list)->int:
    n = my_num_list[0]
    for i in range(len(my_num_list)):
        if n < my_num_list[i]:
            n = my_num_list[i]
    return n

my_num_list = input_date(count_num)
print(my_num_list)
print("Max number = ", max_number(my_num_list))