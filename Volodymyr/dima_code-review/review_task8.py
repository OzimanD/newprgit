'''
list

Переверни світ

Умова: Створи список із назв днів тижня від понеділка до п'ятниці. Зроби так, щоб вони йшли у зворотному порядку (від п'ятниці до понеділка).

Підказка: Можна використати метод списку .reverse() або зробити це за допомогою зрізу [::-1].
'''


list_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

new_list_days = list_days[::-1]
print(new_list_days)
list_days = new_list_days
list_days.reverse()

''' ++ lakonichno
list_days.reverse()
print(list_days)
from Yurii
'''
''' ++ gnuchko
def reverse_list(list_days):
    temp_list = []
    len_list = len(list_days)#len_list = 5
    for i in range(len_list-1, -1, -1):
        temp_list.append(list_days[i])
    return temp_list


list_days = reverse_list(list_days)
print(list_days)
revew from Dima
'''