'''
Задача 10: Сума чисел кратних 3
Напиши програму, яка перебирає всі числа від 1 до 100 включно. Програма має порахувати та вивести суму лише тих чисел,
які діляться на 3 без остачі, але при цьому не діляться на 5.
'''



def count_numbers():
    total = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 != 0:
            total += number
            # print(number)
    return total

print(count_numbers())

'''++Good work!) Using a function wasn't a requirement though, so you could've stopped at just the inner code itself
total = 0
for number in range(1, 101):
    if number % 3 == 0 and number % 5 != 0:
    total += number
print(total)
'''