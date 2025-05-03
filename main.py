class Product:
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity=1):
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_product(self, product, quantity=1):
        if product in self.items:
            new_q = self.items[product] - quantity
            if new_q > 0:
                self.items[product] = new_q
            else:
                del self.items[product]
        else:
            print(f"Produkt {product.name} nie jest w koszyku.")