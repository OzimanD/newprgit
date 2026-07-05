# OOP. 3
# Прізвище
# Вік
# Освіта
# Посада
# Вивести дані про працівників старших 30-ти років, які не мають вищої освіти.

class Employee:
    def __init__(self, name, age, education, position ):
        self.__name = name
        self.__age = age
        self.__education = education
        self.__position = position
    def __str__(self):
        return f"{self.__name},{self.__age},{self.__education},{self.__position}"

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age


    @property
    def education(self):
        return self.__education
    @education.setter
    def education(self, education):
        self.__education = education


    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position):
        self.__position = position


def show_workers_without_higher_education(employees):
    for employee in employees:
        if employee.age > 30 and employee.education != "вища":
            print(employee)

employees = [
    Employee("Іаненко", 35,"середня", "водій"),
    Employee("Петренко", 28,"середня", "слюсар"),
    Employee("Сидоренко", 42, "вища", "інжинер"),
    Employee("Коваленко", 39, "середня", "водій"),

]

show_workers_without_higher_education(employees)

