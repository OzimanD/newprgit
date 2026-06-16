#
# Якщо сума більша за 5000 грн, знижка становить 15%.
#
# В інших випадках знижки немає. Програма має вивести кінцеву суму до сплати.


while True:
    user_sum = input("Введіть сумму покупки: ")
    if user_sum.isdigit():
        user_sum = float(user_sum)
        break
    else:
        print("Не вірне введення, спробуйте знов")


if 5000 > user_sum >= 1000:
    print("Ваша знижка - 10%, до сплати -", user_sum - (user_sum * 0.1))
elif user_sum >= 5000:
    print("Ваша знижка - 15%, до сплати -", user_sum - (user_sum * 0.15))
else:
    print("Не достатня сумма для знижки, до сплати -", user_sum)