class Cake: 
    
    def __init__(self, flavor, size):
        self.flavor = flavor
        self.size = size
    
    def cut_in_parts(self):
        print("Le gâteau est coupé en 4 parts !")
        
    
cake = Cake("chocolate", 5)
print(cake.flavor)
cake.cut_in_parts()

cake.flavor = "banana"
print(cake.flavor)

