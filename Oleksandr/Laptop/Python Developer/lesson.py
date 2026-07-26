import json

# 1. БАЗОВИЙ КЛАС
class Laptop:
    """Базовий клас, що описує загальні характеристики ноутбука."""

    def __init__(self, brand: str, screen_size: float, price: float, ram: int):
        self.__brand = brand
        self.__screen_size = float(screen_size)
        self.__price = float(price)
        self.__ram = int(ram)

    def get_brand(self) -> str:
        return self.__brand

    def get_screen_size(self) -> float:
        return self.__screen_size

    def get_price(self) -> float:
        return self.__price

    def get_ram(self) -> int:
        return self.__ram

    def to_dict(self) -> dict:
        """Серіалізація в словник."""
        return {
            "type": "Laptop",
            "brand": self.get_brand(),
            "screen_size": self.get_screen_size(),
            "price": self.get_price(),
            "ram": self.get_ram()
        }


# 2. ДОЧІРНІЙ КЛАС
class AppleLaptop(Laptop):
    """Дочірній клас з додатковими полями Apple."""

    def __init__(self, screen_size: float, price: float, ram: int, model_name: str, chip_type: str):
        super().__init__(brand="Apple", screen_size=screen_size, price=price, ram=ram)
        self.__model_name = model_name
        self.__chip_type = chip_type

    def get_model_name(self) -> str:
        return self.__model_name

    def get_chip_type(self) -> str:
        return self.__chip_type

    def to_dict(self) -> dict:
        """Серіалізація з розширенням полів."""
        data = super().to_dict()
        data["type"] = "AppleLaptop"
        data["model_name"] = self.get_model_name()
        data["chip_type"] = self.get_chip_type()
        return data


# 3. БІЗНЕС-ЛОГІКА ТА АНАЛІТИКА
def find_max_screen(laptops: list[Laptop]) -> Laptop:
    return max(laptops, key=lambda laptop: laptop.get_screen_size())

def find_min_screen(laptops: list[Laptop]) -> Laptop:
    return min(laptops, key=lambda laptop: laptop.get_screen_size())

def find_cheapest(laptops: list[Laptop]) -> Laptop:
    return min(laptops, key=lambda laptop: laptop.get_price())

def find_most_expensive(laptops: list[Laptop]) -> Laptop:
    return max(laptops, key=lambda laptop: laptop.get_price())

def find_max_ram(laptops: list[Laptop]) -> Laptop:
    return max(laptops, key=lambda laptop: laptop.get_ram())

def find_min_ram(laptops: list[Laptop]) -> Laptop:
    return min(laptops, key=lambda laptop: laptop.get_ram())


# 4. СЕРІАЛІЗАЦІЯ ТА ДЕСЕРІАЛІЗАЦІЯ
def save_laptops_to_json(laptops: list[Laptop], filename: str) -> None:
    data_to_save = [laptop.to_dict() for laptop in laptops]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data_to_save, file, indent=4, ensure_ascii=False)


def load_laptops_from_json(filename: str) -> list[Laptop]:
    with open(filename, "r", encoding="utf-8") as file:
        raw_data = json.load(file)

    restored_laptops: list[Laptop] = []
    for item in raw_data:
        obj_type = item.get("type")
        if obj_type == "AppleLaptop":
            laptop_obj = AppleLaptop(
                screen_size=item["screen_size"],
                price=item["price"],
                ram=item["ram"],
                model_name=item["model_name"],
                chip_type=item["chip_type"]
            )
        elif obj_type == "Laptop":
            laptop_obj = Laptop(
                brand=item["brand"],
                screen_size=item["screen_size"],
                price=item["price"],
                ram=item["ram"]
            )
        else:
            continue
        restored_laptops.append(laptop_obj)

    return restored_laptops


# 5. КЛАС-ІТЕРАТОР (Паттерн «Ітератор»)
class LaptopIterator:
    """Кастомний ітератор для обходу колекції ноутбуків."""

    def __init__(self, laptops: list[Laptop]):
        self._laptops = laptops
        self._index = 0  # Курсор (вказівник на поточний елемент)

    def __iter__(self):
        return self

    def __next__(self) -> Laptop:
        # Якщо вказівник у межах списку — повертаємо елемент і зсуваємо вказівник
        if self._index < len(self._laptops):
            laptop = self._laptops[self._index]
            self._index += 1
            return laptop
        # Якщо елементи закінчилися — зупиняємо ітерацію
        raise StopIteration


# 6. ПЕРЕВІРОЧНИЙ БЛОК ТА ФІНАЛЬНИЙ ВИВІД
if __name__ == "__main__":
    # Створюємо базовий каталог
    laptop_catalog: list[Laptop] = [
        Laptop(brand="Asus", screen_size=17.3, price=1100.0, ram=16),
        Laptop(brand="Lenovo", screen_size=15.6, price=650.0, ram=8),
        Laptop(brand="HP", screen_size=13.3, price=800.0, ram=8),
        AppleLaptop(screen_size=14.2, price=1999.0, ram=18, model_name="MacBook Pro 14", chip_type="M3 Pro"),
        AppleLaptop(screen_size=13.6, price=1099.0, ram=24, model_name="MacBook Air 13", chip_type="M2"),
        AppleLaptop(screen_size=16.2, price=3499.0, ram=36, model_name="MacBook Pro 16", chip_type="M3 Max")
    ]

    # Виконуємо аналітику (знаходимо 6 об'єктів)
    selected_laptops = [
        find_max_screen(laptop_catalog),
        find_min_screen(laptop_catalog),
        find_cheapest(laptop_catalog),
        find_most_expensive(laptop_catalog),
        find_max_ram(laptop_catalog),
        find_min_ram(laptop_catalog)
    ]

    # Зберігаємо у файл
    file_name = "results.json"
    save_laptops_to_json(selected_laptops, file_name)

    # Зчитуємо дані з файлу та відновлюємо об'єкти
    restored_collection = load_laptops_from_json(file_name)

    # Створюємо екземпляр нашого кастомного ітератора
    laptop_iterator = LaptopIterator(restored_collection)

    labels = [
        "1. Найбільший екран",
        "2. Найменший екран",
        "3. Найдешевший ноутбук",
        "4. Найдорожчий ноутбук",
        "5. Найбільше RAM",
        "6. Найменше RAM"
    ]

    print("\n" + "="*55)
    print("      ФІНАЛЬНИЙ ВИВІД РЕЗУЛЬТАТІВ ЧЕРЕЗ ІТЕРАТОР")
    print("="*55)

    # Обхід здійснюється виключно через кастомний ітератор
    label_index = 0
    for laptop in laptop_iterator:
        title = labels[label_index]
        label_index += 1

        print(f"\n[ {title} ]")
        print(f"  • Бренд:     {laptop.get_brand()}")
        print(f"  • Екран:     {laptop.get_screen_size()}\"")
        print(f"  • Ціна:      ${laptop.get_price()}")
        print(f"  • RAM:       {laptop.get_ram()} ГБ")

        # Перевірка специфічних полів дочірнього класу
        if isinstance(laptop, AppleLaptop):
            print(f"  • Модель:    {laptop.get_model_name()}")
            print(f"  • Процесор:  {laptop.get_chip_type()}")

    print("\n" + "="*55)