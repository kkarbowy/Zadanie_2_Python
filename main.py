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
            print(f"Produktu {product.name} nie ma w koszyku.")

    def calculate_total(self):
        return sum(p.price * q for p, q in self.items.items())

    def list_items(self):
        print("Zawartość koszyka:")
        for p, q in self.items.items():
            print(f" - {p.name} x{q}: {p.price:.2f} zł/szt.")

class Order:
    def __init__(self, cart, inventory):
        self.cart = cart
        self.inventory = inventory
        self.status = "Oczekujące"
        self.total = cart.calculate_total()

    def process(self):
        print("Przetwarzanie zamówienia...")
        for prod, qty in self.cart.items.items():
            if self.inventory.get_stock(prod) < qty:
                self.status = "Nieudane"
                print(f"Nie można zrealizować: {prod.name} (potrzeba {qty})")
                return
        for prod, qty in self.cart.items.items():
            self.inventory.remove_stock(prod, qty)
        self.status = "Zrealizowane"
        print("Zamówienie zrealizowane.")

if __name__ == "__main__":
    tshirt = Product("TSH001", "Koszulka Polo - M", 79.99)
    jeans = Product("JNS001", "Jeansy Slim - S", 199.50)
    hat = Product("HT001", "Czapka zimowa - S", 49.00)

    inv = Inventory()
    inv.add_stock(tshirt, 1)
    inv.add_stock(jeans, 5)
    inv.add_stock(hat, 20)

    cart = ShoppingCart()
    cart.add_product(tshirt, 3)
    cart.add_product(jeans, 1)
    cart.remove_product(jeans, 1)
    cart.list_items()
    print(f"Do zapłaty: {cart.calculate_total():.2f} zł\n")

    order = Order(cart, inv)
    order.process()
    print(f"Status zamówienia: {order.status}")
    print(f"Pozostały stan Tshirt: {inv.get_stock(tshirt)} szt.")

    print(f"\nUzupełniam stan koszulek...\n")

    inv.add_stock(tshirt, 15)
    order.process()
    print(f"Status zamówienia: {order.status}")
    print(f"Pozostały stan Tshirt: {inv.get_stock(tshirt)} szt.")