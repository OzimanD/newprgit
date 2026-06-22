class Football:
    def __init__(self, lastname, amplua, age, count_of_games, count_of_goal):
        self.lastname = lastname
        self.amplua = amplua
        self.age = age
        self.count_of_games = count_of_games
        self.count_of_goal = count_of_goal

    def __str__(self):
        return f"{self.lastname} {self.amplua} {self.age} {self.count_of_games} {self.count_of_goal}"

F1 = Football('ln1', 'for', 27, 10, 7)
F2 = Football('ln2', 'wor', 17, 11, 10)
F3 = Football('ln3', 'for', 28, 5, 100)
F4 = Football('ln4', 'zah', 37, 17, 15)
F5 = Football('ln5', 'for', 47, 3, 3)

footbolist = [F1, F2, F3, F4, F5]

def best_forward(footbolist):
    best_f = None
    max_goal = 0
    for gravec in footbolist:
        if gravec.amplua =='wor' and gravec.count_of_goal>max_goal:
            max_goal = gravec.count_of_goal
            best_f = gravec
    return best_f

print(best_forward(footbolist))

