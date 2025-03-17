
from product_manager import ProductManager
from product import Product
from cart import Cart
import random

manager = ProductManager()

manager.add_product(Product("Laptop", 1000, 10))
manager.add_product(Product("Keyboard", 250.50, 5))
manager.add_product(Product("Mouse", 150, 20))
manager.add_product(Product("Tablet", 1000, 10))
manager.add_product(Product("USB Cable", 10.20, 10))

print()
print("INVENTORY / Products list: \n-----------------")
manager.display_products()

print(f"\n\tTotal list products value: {manager.total_value_products():.2f}")


print()
cart = Cart()

print("CART\n-----------------")
products = manager.product_list
for _ in range(3):
    product = random.choice(products)  
    max_quantity = min(product.quantity, 3)  
    if max_quantity > 0:
        quantity = random.randint(1, max_quantity)  
        cart.add_product_to_cart(product, quantity)


print("\nCart contents:")
cart.display_cart()

print(f"\nTotal cart value: ${cart.cart_total_spent():.2f}")

print()




