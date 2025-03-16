
from product_manager import ProductManager
from product import Product

manager = ProductManager()

manager.add_product(Product("Laptop", 1000, 2))
manager.add_product(Product("Keyboard", 250.50, 2))
manager.add_product(Product("Mouse", 150, 4))
manager.add_product(Product("Tablet", 1000, 3))
manager.add_product(Product("USB Cable", 10.20, 1))

print()
print("Products list: ")
manager.display_products()

print(f"\nTotal list products value: {manager.total_value_products():.2f}")


print()



