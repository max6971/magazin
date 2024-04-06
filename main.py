class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Инициализация пустого словаря для хранения товаров

    def add_item(self, item_name, price):
        """Метод для добавления товара в ассортимент."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Метод для удаления товара из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        """Метод для получения цены товара по его названию."""
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        """Метод для обновления цены товара."""
        if item_name in self.items:
            self.items[item_name] = new_price

stores = []

def add_store():
    name = input("Введите название магазина: ")
    address = input("Введите адрес магазина: ")
    store = Store(name, address)
    stores.append(store)
    print(f"Магазин '{name}' добавлен.")