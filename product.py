
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return f"{self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}"
    
    def set_quantity(self, new_quantity):
        self.quantity += new_quantity
        if self.quantity < 0:
            self.quantity = 0 
            print(f"Quantity for {self.name} cannot be negative. Setting to 0.")
            
        
    

