#Прізвище
#Вік
#Кількість ігор
#Кількість пропущених шайб

#Визначити середній вік хокеїстів і вивести відомості про хокеїстів, вік яких понад 25 років.
class Hockey:
    def __init__(self, surname, age, number_of_games, number_of_missing_goals):
        self.__surname = surname
        self.__age = age
        self.__number_of_games = number_of_games
        self.__number_of_missing_goals = number_of_missing_goals

    @property
    def get_surname(self):
        return self.__surname

    @property
    def get_age(self):
        return self.__age

    @property
    def get_number_of_games(self):
        return self.__number_of_games

    @property
    def get_number_of_missing_goals(self):
        return self.__number_of_missing_goals

    @get_number_of_games.setter
    def set_games(self, games):
        if games >= 0:
            self.__number_of_games = games
        else:
            raise ValueError("Кількість ігор не може бути від'ємною")

    @get_age.setter
    def set_age(self, age):
        self.__age = age

    @get_number_of_games.setter
    def set_games(self, games):
        if games >= 0:
            self.__number_of_games = games
        else:
            raise ValueError("Кількість ігор не може бути від'ємною")

    @get_number_of_missing_goals.setter
    def set_games(self, goals):
        if goals >= 0:
            self.__number_of_missing_goals = goals
        else:
            raise ValueError("Кількість пропущених голів не може бути від'ємною")

    def __str__(self):
            return f"{self.__surname}, {self.__age}, {self.__number_of_games}, {self.__number_of_missing_goals}"

h1 = Hockey('Варава', 25, '12', '2')
h2 = Hockey('Дахновський', 21, '8', '3')
h3 = Hockey('Пасько', 20, '17', '1')
h4 = Hockey('Бабинець', 38, '11', '4')
h5 = Hockey('Трошкін', 27, '16', '9')

def analyze_hockey_players(players_list):

    total_age = 0
    older_than_25 = []

    for player in players_list:
        total_age += player.get_age

        if player.get_age > 25:
            older_than_25.append(player)

    average_age = total_age / len(players_list)

    print(f"Середній вік хокеїстів: {average_age:.1f} років\n")

    print("Хокеїсти, яким понад 25 років:")
    if older_than_25:
        for player in older_than_25:
            print(player)
    else:
        print("Таких гравців немає.")


players = []
try:
    result = analyze_hockey_players(players)
    if result:
        print(result)
except:
    print("Список хокеїстів порожній.")






