
from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []
        
    def add_product_to_cart(self, product, quantity):
        if quantity < product.quantity:
            self.cart_items.append({"product": product, "quantity": quantity})
            product.set_quantity(-quantity)
        else:
            print("Insufficient stock!")
        

    def cart_total_spent(self):
        return sum(item["product"].price * item["quantity"] for item in self.cart_items)
 
    def display_cart(self):
        if len(self.cart_items) == 0:
            print("Cart is empty.")
        else:
            for item in self.cart_items:
                print(f"Product: {item["product"].name} - {item["quantity"]} = {item["product"].price * item["quantity"]}")
