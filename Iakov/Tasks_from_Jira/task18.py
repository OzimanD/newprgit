#Клуб любителів книг

#Умова: Є дві множини студентів: ті, хто прочитав першу книгу, і ті,
# хто прочитав другу. Знайди тих студентів, які прочитали обидві книги.

#Підказка: Для пошуку спільних елементів використовуй оператор амперсанд & або метод .intersection().
def function_intersection(student1, student2):
    intersection = student1.intersection(student2)
    return intersection

student1 = {1,2,3,4,5}
student2 = {4,5,6,7,8}
intersection = function_intersection(student1, student2)
print(intersection)
