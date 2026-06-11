def salary_bonus(salary, years):
    if years >= 2 and years < 5:
        bonus = salary * 2 / 100
    elif years >= 5 and years <= 10:
        bonus = salary * 5 / 100
    else:
        bonus = 0

    total_salary = salary + bonus

    return bonus, total_salary


salary = float(input("Введіть зарплату: "))
years = int(input("Введіть стаж: "))

bonus, total_salary = salary_bonus(salary, years)

print("Надбавка:", bonus)
print("Сума до виплати:", total_salary)