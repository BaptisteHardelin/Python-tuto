class Human:
    def run (self):
        print("Je cours !")
        
class Lion:
    def run (self):
        print("Je suis le roi de la savane !")
        
class Fish:
    def swim (self):
        print("Je nage !")
        
entities = [Human(), Lion(), Fish()]

for entity in entities:
    entity.run()