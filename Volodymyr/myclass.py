# print("Hello world")
#super

'''
Розрахувати надбавку до зарплати за стаж: якщо стаж становить від 2 до 5 років, 
надбавка дорівнює 2%; якщо стаж становить від 5 до 10 років — 5%. 
Ввести з клавіатури зарплату та стаж, вивести надбавку та суму до виплати.
'''
# def work_bonus(salary, work_experience):
#
#     if 2 <= work_experience <= 5:
#         print("Your bonus is 2%")
#         bonus_in_percent = 2
#     elif 5 <= work_experience <= 10:
#         print("Your bonus is 5%")
#         bonus_in_percent = 5
#     else:
#         print("You dont have any bonus")
#         bonus_in_percent = 0
#
#     bonus = salary * bonus_in_percent / 100 #добавил бы скобочки (salary) * (bonus_in_percent)
#     full_salary = salary + bonus
#     return bonus, full_salary
#
#
# salary = float(input("Enter your salary: "))
# work_experience = float(input("Enter your work experience in years: "))
#
# salary_result = work_bonus(salary, work_experience)
#
# print("Bonus: ", salary_result[0])
# print("Total bonus: ", salary_result[1])


'''
1 Даны два целых числа A и B (A < B). 
Найти все целые числа, расположенные между данными числами (включая сами эти числа), в порядке их возрастания, 
а также количество N этих чисел.
'''

def new_numbers(A, B):
    print_number = 0

    for number in range(A, B + 1):
        print(number)
        print_number += 1
    return print_number

A = int(input("Enter your first number: "))
B = int(input("Enter your second number: "))

print_number = new_numbers(A, B)

print(f"Amount of numbers: {print_number}")
