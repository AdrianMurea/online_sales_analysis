
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return f"{self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}"
    
    def set_quantity(self, new_quantity):
        if new_quantity > 0:
            self.quantity += new_quantity
        else:
            print("Quantity must be positive")
            
        
    

