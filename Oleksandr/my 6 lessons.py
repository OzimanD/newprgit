# OOP. 1
# Прізвище
# Рік народження
# Посада
# Зарплата
# Освіта
# Визначити наймолодшого працівника та надрукувати відомості про нього.

class Worker:
    def __init__(self, surname, birth_year, position, salary, education):
        self.__surname = surname
        self.__birth_year = birth_year
        self.__position = position
        self.__salary = salary
        self.__education = education

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def birth_year(self):
        return self.__birth_year

    @birth_year.setter
    def birth_year(self, birth_year):
        self.__birth_year = birth_year

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    @property
    def education(self):
        return self.__education

    @education.setter
    def education(self, education):
        self.__education = education

    def __str__(self):
        return f"{self.__surname}, {self.__birth_year}, {self.__position}, {self.__salary}, {self.__education}"


w1 = Worker("Іваненко", 1985, "водій", 28000, "середня спеціальна")
w2 = Worker("Петренко", 2001, "програміст", 45000, "вища")
w3 = Worker("Сидоренко", 1997, "бухгалтер", 37000, "вища")
w4 = Worker("Коваленко", 1992, "менеджер", 32000, "середня спеціальна")
w5 = Worker("Мельник", 2003, "оператор", 26000, "середня")


workers = [w1, w2, w3, w4, w5]


def show_youngest_worker(workers):
    youngest_worker = workers[0]

    for worker in workers:
        if worker.birth_year > youngest_worker.birth_year:
            youngest_worker = worker

    print("Наймолодший працівник:")
    print("Прізвище:", youngest_worker.surname)
    print("Рік народження:", youngest_worker.birth_year)
    print("Посада:", youngest_worker.position)
    print("Зарплата:", youngest_worker.salary)
    print("Освіта:", youngest_worker.education)


show_youngest_worker(workers)