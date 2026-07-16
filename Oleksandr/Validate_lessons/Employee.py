import re

class Employee:
    def __init__(self, lastname,birth_year,position,salary,education):
        self.__lastname = lastname
        self.__birth_year = birth_year
        self.__position = position
        self.__salary = salary
        self.__education = education

    def __validate_lastname(self,value):
        if not isinstanse(value,str) or not re.fullmatch(r"[A-Za-zA-Яа-яІіЇїЄєҐґ]{2,}",value):
            raise ValueError("Некоректне прізвище")
        return value
    def __validate_birth_year(self,value):
        if not isinstanse(value,int) or value <1900 or value >2026:
            raise ValueError("Рік народження має бути від 1900 до 2026")
        return value
    def __validate_position(self,value):
        if not isinstanse(value, str) or len(value) < 2:
            raise ValueError("Некоректна посада")
        return value
    def __validate_salary(self,value):
        if not isinstanse(value,int) or value <0:
            raise ValueError("Зарплата не може бути відємною")
        return value
    def __validate_education(self,value):
        if not isinstanse(value,str) or len(value) <2:
            raise ValueError("Некоректна освіта")
        return value

    @property
    def lastname(self): return self.__lastname
    @property
    def birth_year(self): return self.__birth_year
    @property
    def position(self): return self.__position
    @property
    def salary(self): return self.__salary
    @property
    def education(self): return self.__education

    @salary.setter
    def salary(self,value):
        self.__salary = self.__validate_salary(value)

    def age(self):
        return 2026-self.birth_year

    def __str__(self):
        return (f"Прізвище:{self.__lastname},рік:{self.__birth_year},"
                f"вік:{self.age()},поса:{self.__position},"
                f"зарплата: {self.__salary},освіта:{self.__education}")



