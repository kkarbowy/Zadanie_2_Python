class Product:
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self._stock = {}

    def add_stock(self, product, quantity):
        current = self._stock.get(product, 0)
        self._stock[product] = current + quantity

    def remove_stock(self, product, quantity):
        available = self._stock.get(product, 0)
        if quantity > available:
            print(f"Brak towaru: {product.name} (dostępne {available})")
            return False
        self._stock[product] = available - quantity
        return True

    def get_stock(self, product):
        return self._stock.get(product, 0)