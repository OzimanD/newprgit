# Сценарій: Ми рахуємо кількість однакових слів у списку за допомогою словника. Я
# кщо слова ще немає в словнику — додаємо його з лічильником 1,
# якщо є — збільшуємо лічильник. Але код падає з помилкою KeyError.

words = ["apple", "banana", "apple", "cherry", "banana", "banana"]
# word_count = {}
word_count = dict() # empty dict - it is more reliably

for word in words:
    if word in word_count: # Отут щось іде не так
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
