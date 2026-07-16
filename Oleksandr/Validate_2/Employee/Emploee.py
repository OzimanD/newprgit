# Прізвище Ім'я По батькові
# Посада
# Зарплата
# Дата народження
# Вивести відомості про працівників, у яких зарплата вища за середню і вік менше 30-ти років.

class Employee:
    def __init__(self,lastname,name,middle_name,position,salary, birth_year):
        self.__lastname = lastname
        self.__name = name
        self.__middle_name = middle_name
        self.__position = position
        self.__salary = salary
        self.__birth_year = birth_year

    @property
    def lastname(self):
        return self.__lastname
    @property
    def name(self):
        return self.__name
    @property
    def middle_name(self):
        return self.__middle_name
    @property
    def position(self):
        return self.__position
    @property
    def salary(self):
        return self.__salary
    @property
    def birth_year(self):
        return self.__birth_year

    @lastname.setter
    def lastname(self,lastname):
        self.__lastname = lastname
    @name.setter
    def name(self,name):
        self.__name = name
    @middle_name.setter
    def middle_name(self,middle_name):
        self.__middle_name = middle_name
    @position.setter
    def position(self,position):
        self.__position = position
    @salary.setter
    def salary(self,salary):
        self.__salary = salary


def __str__(self):
    return (f"{self.__lastname},{self.__name},{self.__position}, {self.__salary}, {self.__birth_year},{self.__middle_name}")

