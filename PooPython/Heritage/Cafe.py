class Drink:
    """Une boisson"""
    
    def __init__(self, price):
        """On initialise le prix"""
        self.price = price
        
    def drink(self):
        """Boire la boisson"""
        print("Je ne sais pas ce que c'est, mais je le bois.")
        

class Coffee(Drink):
    """Café"""
    
    prices = {"simple": 1, "serré": 2, "allongé": 1.5}
    
    def __init__(self, type):
        """On initialise le type de café"""
        self.type = type
        super().__init__(price = self.price.get(type, 1))
        
    def drink(self):
        """Boire le café"""
        print("Un bon café pour me réveiller !")