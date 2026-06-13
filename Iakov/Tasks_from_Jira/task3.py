#def remove_evens(numbers):
   # for num in numbers:
       # if num % 2 == 0:
           # numbers.remove(num)
   # return numbers

# Тест: очікуємо [1, 3, 5, 7]
#print(remove_evens([1, 2, 2, 3, 4, 5, 6, 7]))
# Що виводить насправді: [1, 2, 3, 5, 7] — одна двійка залишилась! Why?


# Правильний варіант коду -
def remove_evens(numbers):
    result = []

    for num in numbers:
        if num % 2 != 0:
            result.append(num)

    return result

# Тест: очікуємо [1, 3, 5, 7]
print(remove_evens([1, 2, 2, 3, 4, 5, 6, 7]))
# Що виводить насправді: [1, 2, 3, 5, 7] — одна двійка залишилась! Why?