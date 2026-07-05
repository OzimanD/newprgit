# OOP. Хокеїсти
# Прізвище
# Вік
# Кількість ігор
# Кількість пропущених шайб
# Визначити середній вік хокеїстівs
# і вивести відомості про хокеїстів, вік яких понад 25 років.


class HockeyPlayer:
    def __init__(self, surname, age, games, missed_pucks):
        self.__surname = surname
        self.__age = age
        self.__games = games
        self.__missed_pucks = missed_pucks

    def __str__(self):
        return f"{self.__surname}, {self.__age}років, ігор:{self.__games}, пропущених шайб:{self.__missed_pucks}"

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def games(self):
        return self.__games
    @games.setter
    def games(self, games):
        self.__games = games

    @property
    def missed_pucks(self):
        return self.__missed_pucks
    @missed_pucks.setter
    def missed_pucks(self, missed_pucks):
        self.__missed_pucks = missed_pucks

def average_age(players):
    total = 0
    for player in players:
        total += player.age

    return total/len(players)

def players_older_than_25(players):
    for player in players:
        if player.age > 25:
            yield player

players = [
    HockeyPlayer("Puaro", 25, 15,99),
    HockeyPlayer("Ronald", 9, 45,22),
    HockeyPlayer("Pele", 27, 80,46),
    HockeyPlayer("Rosald", 44, 17,888),
    HockeyPlayer("Qudae", 122, 333,674),
]

avg = average_age(players)

print("Середній вік хокеїстів:",avg)

print("Хокеїсти,вік яких понад 25 років:")
for player in players_older_than_25(players):
    print(player)






