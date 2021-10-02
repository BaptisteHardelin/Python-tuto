class Cat:
    """Un chat"""
    
    def meow(self):
        """Miaule"""
        print("Meow !")
        
class Talker:
    """Interface qui définit la méthode say"""
    def say(self, to_say):
        """Affiche to_say"""
        print(to_say)
        
class TalkingCat(Cat, Talker):
    """Un chat qui parle ?"""
    pass

animal = TalkingCat()
animal.meow()
animal.say("Hello world")