'''
Завдання 10: Секретний шифр (Тема: Конкатенація рядків у циклі)
Сценарій: Функція має подвоювати кожну літеру в рядку (наприклад, "cat" -> "ccaatt"). Але код падає з TypeError: can only concatenate str (not "int") to str.
'''
def double_letters(text):
    result = ""
    for i in range(len(text)):
        result += text[i] * 2
    return result

print(double_letters("py"))
'''
Увага: у цьому коді є нюанс — сам по собі він спрацює, але що буде, якщо логіка обходу зміниться? Давай подивимось на інший варіант, де точно є помилка:
'''
def double_letters_v2(text):
    result = ""
    for char in text:
        result += char * 2 # Отут помилка!
    return result

print(double_letters_v2("py"))
'''
Підказка: Python не вміє автоматично додавати числа до рядків (на відміну від деяких інших мов). Як повторити рядок кілька разів або як правильно зробити дублювання символу?
'''