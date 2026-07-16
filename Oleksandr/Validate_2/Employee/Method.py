from unittest import result

from Objects import *
# Вивести відомості про працівників, у яких зарплата вища за середню і вік менше 30-ти років.
def count_workers_older_30(employees):
    listresult = []
    avg = 0
    for emp in employees:
        avg += emp.salary
    avg = avg/len(employees)

    for emp in employees:
        if(2026-emp.birth_year) <=30 and (emp.salary>avg):
            listresult.append(emp)
    return listresult

res = count_workers_older_30(employees)
for i in res:
    print(res)







