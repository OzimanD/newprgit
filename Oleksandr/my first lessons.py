# Виконавець
# Жанр
# Назва
# альбому
# Тираж
# Вивести дані про платівки, тираж яких перевищує
# 10000примірників.


# 1 створення класу із назвою
class Actor:
    # 2 ініціалізація конструктора
    def __init__(self, janr, name, album, tiraj):
        self.__janr = janr
        self.__name = name
        self.__album = album
        self.__tiraj = tiraj
    # 3 Організація виводу
    def __str__(self):
        return f"{self.__janr},{self.__name},{self.__album},{self.__tiraj}"
    # 4 Геттери та сеттери обовязково
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def album(self):
        return self.__album

    @album.setter
    def album(self, value):
        self.__album = value

    @property
    def tiraj(self):
        return self.__tiraj

    @tiraj.setter
    def tiraj(self, value):
        self.__tiraj = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

# 5 Створення обєктів
a1 = Actor("kloun", "Ivan", "sammer2026", 1990)
a2 = Actor("veduchii", "Oleg", "sammer2026", 99999)
a3 = Actor("balerina", "Svitlana", "sammer2026", 82873)
a4 = Actor("dancer", "Valerii", "sammer2026", 55555)
a5 = Actor("sufler", "Victor", "sammer2026", 33777)
#  6 Створення масиву обєктів
actor = [a1, a2, a3, a4, a5]
print(actor)


# Вивести дані про платівки, тираж яких перевищує
# 10000примірників.

#7 Створення функції для створення результатів задачі
def search(actor):
    result = []
    for actor_1 in actor:
        if actor_1.tiraj >= 10000:
            result.append(actor_1)
    return result

print(search(actor))
#8 вивід результатів до консолі
result = search(actor)
for actor_1 in result:
    print(actor_1)












