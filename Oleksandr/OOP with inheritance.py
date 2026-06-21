
# OOP. 1
# Поля
# Найменування
# Кількість
# Ціна
# Виробник
# Дата_надходження_на_склад
# Визначити кількість усіх товарів, кількість яких більша за 5 і вивести відомості про ці товари.

class Product:
    def __init__(self,name):
        self.name = name

class ConcreteProduct(Product):
    def __init__(self,name,count,price,manufacturer,date):
        super().__init__(name)
        self.name = name
        self.count = count
        self.price = price
        self.manufacturer = manufacturer
        self.date = date


