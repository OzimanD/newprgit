from Objects import *


def count_workers_older_60(employees):
    count = 0

    for employee in employees:
        if employee.age() > 60:
            count += 1

    return count


def print_workers(employees):
    iterator = iter(employees)

    for employee in iterator:
        if employee.age() > 60:
            print(employee)


def write_file(employees):
    file = open("result.txt", "w", encoding="utf-8")

    iterator = iter(employees)

    for employee in iterator:
        if employee.age() > 60:
            file.write(str(employee) + "\n")

    file.write(
        "Кількість працівників старших за 60 років: "
        + str(count_workers_older_60(employees))
        + "\n"
    )

    file.close()


def read_file():
    file = open("result.txt", "r", encoding="utf-8")

    print(file.read())

    file.close()