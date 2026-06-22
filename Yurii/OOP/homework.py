# OOP. 1
# Поля
# Найменування
# Кількість
# Ціна
# Виробник
# Дата_надходження_на_склад
# ### функция повертаэ лист кість усіх товарів, кількість яких більша за 5 і вивести відомості про ці товари.
# класс продакт Найменування
# класс конкретний продукт успадкувати вид продакт

import datetime

class Product:
    top_product_name = list()
    def __init__(self, name, model, amount, price, receipt_date):
        self.name = name
        self.model = model
        self.amount = amount
        self.price = price
        self.receipt_date = receipt_date


    def quantity(self):

        if self.amount > 5:
            self.top_product_name.append(self.model)
        print(self.top_product_name)

class Router(Product):
    def __init__(self, name, model, amount, price, receipt_date, vendor):
        super().__init__(name, model, amount, price, receipt_date)
        self.vendor = vendor

class Laptop(Router):
    def __init__(self, name, model, amount, price, receipt_date, vendor, ram, hard_disk, screen_size):
        super().__init__(name, model, amount, price, receipt_date, vendor)
        self.ram = ram
        self.hard_disk = hard_disk
        self.screen_size = screen_size

class EBook(Product):
    def quantity(self):
        if self.receipt_date < str(datetime.date(2021, 1, 1)):
            print(f"{self.name} : {self.model}- цей продукт застарів, "
                    f"випущений в {self.receipt_date}  - "
                    f"{(datetime.date.today() - datetime.datetime.strptime(self.receipt_date,'%Y-%m-%d').date()).days//365} років тому")

router = Router('Router', "Linksys e2500", 7, 5200, "2026-06-20", 'cisco')
Router.quantity(router)
notebook = Laptop( 'Laptop', "Dell XPS 15", 22, 78000, "2026-01-22", 'Dell',
                   32, 512, 15)
Laptop.quantity(notebook)
e_book = EBook('eBook', 'Sony', 100, 3500, "2020-02-25")
EBook.quantity(e_book)

