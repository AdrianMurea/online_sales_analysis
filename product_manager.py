
class ProductManager:
    def __init__(self):
        self.product_list = []
        
    def add_product(self, product):
        self.product_list.append(product)
    
    def display_products(self):
        if len(self.product_list) == 0:
            print("List product is empty.")
        else:
            for product in self.product_list:
                print(product)
    
    def total_value_products(self):
        return sum(item.price*item.quantity for item in self.product_list)
