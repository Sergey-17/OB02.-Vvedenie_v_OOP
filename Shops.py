class Store:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name: str, price: float) -> None:
        """Добавляет товар в ассортимент магазина."""
        self.items[item_name] = price

    def remove_item(self, item_name: str) -> None:
        """Удаляет товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name: str) -> float | None:
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name)

    def update_price(self, item_name: str, new_price: float) -> None:
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price


# Создание объектов магазинов
store1 = Store("Продуктовый рай", "ул. Ленина, 10")
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store1.add_item("молоко", 1.2)

store2 = Store("ТехноМир", "пр. Мира, 25")
store2.add_item("ноутбук", 999.99)
store2.add_item("смартфон", 499.99)
store2.add_item("наушники", 99.99)

store3 = Store("Книжная лавка", "ул. Пушкина, 5")
store3.add_item("роман", 15.5)
store3.add_item("детектив", 12.3)
store3.add_item("фэнтези", 18.0)

# Тестирование методов на одном из магазинов (store1)
print(f"Магазин: {store1.name}, Адрес: {store1.address}")
print("Текущий ассортимент:", store1.items)

# Добавление товара
store1.add_item("хлеб", 0.9)
print("После добавления хлеба:", store1.items)

# Обновление цены
store1.update_price("яблоки", 0.6)
print("После обновления цены яблок:", store1.items)

# Получение цены товара
print("Цена бананов:", store1.get_price("бананы"))
print("Цена несуществующего товара:", store1.get_price("печенье"))

# Удаление товара
store1.remove_item("молоко")
print("После удаления молока:", store1.items)