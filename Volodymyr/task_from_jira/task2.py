'''
=== ЗАДАЧІ НА СПИСКИ (LIST) ===

Топ-3 геймера

Умова: Є список оцінок або балів гравців: [45, 82, 12, 95, 67, 88]. Знайди та виведи три найвищі результати.

Підказка: Спочатку відсортуй список за спаданням за допомогою .sort(reverse=True) або функції sorted(), а потім візьми зріз [:3].
'''
score_list = [45, 82, 12, 95, 67, 88]

# new_score_list = sorted(score_list, reverse=True)
# print(new_score_list[:3])
# variant 2
score_list.sort(reverse=True)
print(score_list[:3])
# variant 3
for i in range(3):
    print(max(score_list), end=' ')
    score_list.remove(max(score_list))


