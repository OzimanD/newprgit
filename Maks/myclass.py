# Розрахувати надбавку до зарплати за стаж: якщо стаж становить від 2 до 5 років, надбавка дорівнює 2%;
# якщо стаж становить від 5 до 10 років — 5%.
# Ввести з клавіатури зарплату та стаж, вивести надбавку та суму до виплати.




def pay_bonus(pay_sum,experience):
    match experience:
        case experience if experience < 2:
            print("Замалий стаж, без надбавки. Зарплата -", pay_sum)
        case experience if 2 <= experience <= 5:
            print("Стаж 2 - 5 років, надбавка - 2%. Зарплата -", pay_sum + (pay_sum * 0.02))
        case experience if 5 < experience <= 10:
            print("Стаж 5 - 10 років, надбавка - 5%. Зарплата -", pay_sum + (pay_sum * 0.05))
        case _:
            print("Не правильний ввід")


salary = float(input("Введіть зарплату: "))
experience = float(input("Введіть стаж: "))
pay_bonus(salary,experience)

#DONE!