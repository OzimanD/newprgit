#Дано два цілі числа A і B, причому A < B.
#Потрібно вивести всі цілі числа від A до B включно у порядку зростання,
#а також вивести кількість цих чисел N.

def count_number(a, b):
        if a >= b:
            print("Значення чисел не відповідають умові A, спробуйте ще раз")
            return 1
        else:
            n = 0
            for number in range(a, b + 1):
                print(number)
                n += 1
            print("Кількість чисел N:", n)


while True:
    a = int(input("Введіть число A: "))
    b = int(input("Введіть число B (більше за A): "))
    if count_number(a,b) != 1:
        break
