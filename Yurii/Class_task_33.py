# ’Задача 2: Пароль з трьох спроб
# Програма має перевіряти пароль (вигадай будь-який наперед).
# У користувача є рівно 3 спроби, щоб ввести його правильно.
# Якщо пароль вірний — вивести «Доступ дозволено» і зупинити роботу.
# Якщо користувач помилився 3 рази — вивести «Акаунт заблоковано».


bd_login_password = {'admin': '123456',
                     'user': 'qwerty',
                     'Admin': 'QAZwsx',
                     'User': '1qaz2wsx',}


def check_credentials(login, password):
    try:
        if bd_login_password[login] == password: ### bd_login_password.get(login) == password:
            #print('True')
            return True
        else:
            #print('False')
            return False
    except KeyError:
        print(f"Такого користувача не існує!")
        return False

def main():
    try:
        num_attempts = 3
        counter = 1
        while counter <= num_attempts:
            login = input("Введіть свій логін: ")
            password = input("Введіть свій пароль: ")
            if check_credentials(login, password):
                print(f"Авторизацію успішно пройдено з {counter}-ї спроби")
                break
            elif counter == num_attempts:
                print(f"Ви використали {counter} спроби. Спробуйте відновити пароль!")
                break
            else:
                print("Спробуйте ще раз.")
                counter += 1
    except NameError:
        pass



if __name__ == '__main__':
    main()