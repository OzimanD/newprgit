print("hello world")
print("hello world")
print("hello world")


# task 1
def salary_bonus(salary, experience):
    bonus = 0

    if 2 <= experience < 5:
        bonus = salary * 0.02
    elif 5 <= experience < 10:
        bonus = salary * 0.05

    total = salary + bonus

    return bonus, total


salary = float(input("Введіть зарплату: "))
experience = float(input("Введіть стаж (років): "))

bonus, total = salary_bonus(salary, experience)

print("Надбавка:", bonus)
print("До виплати:", total)

# task 2
def main(a, b):
    count = 0

    for i in range(a, b + 1):
        print(i)
        count += 1

    return count


a = int(input("Введіть число A: "))
b = int(input("Введіть число B: "))

n = main(a, b)

print("Кількість чисел:", n)