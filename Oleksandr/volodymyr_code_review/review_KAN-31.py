"""Зрозумів, тримай чисті текстові задачі на умови та цикли. Ніякого готового коду, тільки умови,
які треба реалізувати з нуля.
Задача 1: Калькулятор знижок
Напиши програму, яка запитує у користувача суму покупки.
Якщо сума більша за 1000 грн, нараховується знижка 10%.
Якщо сума більша за 5000 грн, знижка становить 15%.
В інших випадках знижки немає. Програма має вивести кінцеву суму до сплати.
"""

price = float(input("Введіть суму покупки:"))

if price > 5000:
    discount_percent = 15
elif price > 1000:
    discount_percent = 10
else:
    discount_percent = 0

discount = price * discount_percent / 100
final_price = price - discount

print("Знижка:" discount)
print("До сплати:", final_price)
 #






"""
price = float(input("Введіть суму покупки:"))


def book_sales(book_price):
    if book_price > 5000:
        print("You have 15% discount")
        book_discount = 15 / 100
    elif book_price > 1000:
        print("You have 10% discount")
        book_discount = 10 / 100
    else:
        print("You have 0% discount")
        book_discount = 0 / 100
        
    discount = book_discount * book_price
    final_price = book_price - discount

    return final_price
    
    
final_book_price = book_sales(price)
print("your final book price is",  final_book_price)


# Your solution for task 31 is correct, but you can also put the if clause inside a function so you can reuse it for different types of discounts and different books.


# You forgot to put a comma in line 22 before discount:
print("Знижка:", discount)
"""