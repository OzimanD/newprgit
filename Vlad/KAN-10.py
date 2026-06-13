words = ["apple", "banana", "apple", "cherry", "banana", "banana"]
word_count = {}

for word in words:
    if word in word_count: # Отут щось іде не так
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)