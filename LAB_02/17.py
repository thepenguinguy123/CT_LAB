class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
class Order:
    def __init__(self):
        self.items = []  
        self.discount = 0.0
    def add_product(self, product, quantity):
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        if product.stock < quantity:
            print(f"Not enough stock for {product.name}. Only {product.stock} left.")
            return
        product.stock -= quantity
        self.items.append((product, quantity))
        print(f"Added {quantity} x {product.name} to order.")
    def apply_discount(self, percent):
        if percent < 0 and percent > 100:
            raise ValueError("Discount percent must be between 0 and 100.")
        self.discount = percent
        print(f"Discount of {percent}% applied.")
    def get_total(self):
        total = sum(product.price * quantity for product,quantity in self.items)
        total_after_discount = total * (1 - self.discount / 100)
        return total_after_discount
    def print_invoice(self):
        print("\n=== ORDER ===")
        for product, quantity in self.items:
            subtotal = product.price * quantity
            print(f"{quantity} x {product.name} = ${subtotal:.2f}")
        print(f"Discount: {self.discount}%")
        print(f"Total: ${self.get_total():.2f}")
        print("=====================")

p1 = Product("Laptop", 1500, 10)
p2 = Product("Mouse", 25, 50)
p3 = Product("Keyboard", 60, 30)

order = Order()
order.add_product(p1, 2)
order.add_product(p2, 3)
order.add_product(p3, 1)

order.apply_discount(10)
order.print_invoice()
