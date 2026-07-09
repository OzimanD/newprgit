# OOP. 2
# Прізвище
# Група
# Рік народження
# оцінка з фізики
# оцінка з математики
# оцінка з інформатики
# Надрукувати прізвища студентів, які склали математику на «95», і визначити їхню кількість.

class Student:
    def __init__(self, surname, group, birth_year, physics_mark, math_mark, informatics_mark):
        self.__surname = surname
        self.__group = group
        self.__birth_year = birth_year
        self.__physics_mark = physics_mark
        self.__math_mark = math_mark
        self.__informatics_mark = informatics_mark

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group):
        self.__group = group

    @property
    def birth_year(self):
        return self.__birth_year

    @birth_year.setter
    def birth_year(self, birth_year):
        self.__birth_year = birth_year

    @property
    def physics_mark(self):
        return self.__physics_mark

    @physics_mark.setter
    def physics_mark(self, physics_mark):
        self.__physics_mark = physics_mark

    @property
    def math_mark(self):
        return self.__math_mark

    @math_mark.setter
    def math_mark(self, math_mark):
        self.__math_mark = math_mark

    @property
    def informatics_mark(self):
        return self.__informatics_mark

    @informatics_mark.setter
    def informatics_mark(self, informatics_mark):
        self.__informatics_mark = informatics_mark

    def __str__(self):
        return f"{self.__surname}, {self.__group}, {self.__birth_year}, фізика: {self.__physics_mark}, математика: {self.__math_mark}, інформатика: {self.__informatics_mark}"


s1 = Student("Іваненко", "П-21", 2005, 88, 95, 91)
s2 = Student("Петренко", "П-21", 2004, 76, 82, 89)
s3 = Student("Сидоренко", "П-22", 2005, 90, 95, 94)
s4 = Student("Коваленко", "П-22", 2003, 70, 75, 80)
s5 = Student("Мельник", "П-23", 2006, 96, 95, 98)


students = [s1, s2, s3, s4, s5]


def find_students_with_math_95(students):
    result = []

    for student in students:
        if student.math_mark == 95:
            result.append(student)

    return result


def print_result_with_iterator(result_students):
    print("Студенти, які склали математику на 95:")

    iterator = iter(result_students)
    count = 0

    while True:
        try:
            student = next(iterator)
            print(student.surname)
            count += 1
        except StopIteration:
            break

    print("Кількість студентів:", count)


def write_result_to_file(result_students, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("Студенти, які склали математику на 95:\n")

        iterator = iter(result_students)
        count = 0

        while True:
            try:
                student = next(iterator)
                file.write(student.surname + "\n")
                count += 1
            except StopIteration:
                break

        file.write("Кількість студентів: " + str(count) + "\n")


def read_file_to_console(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()
        print(text)


result_students = find_students_with_math_95(students)

print_result_with_iterator(result_students)

write_result_to_file(result_students, "result.txt")

print("\nДані з файлу:")
read_file_to_console("result.txt")