class Film:
    def __init__(self, name):
        self.name = name
        
    def watch (self, player):
        print("Bon film !")
        
        
class FilmCassette(Film):
    def __init__(self, name):
        """On initialise le nom et la bande magnetique"""
        super().__init__(name)
        self.magnetic_tap = True
        
    def to_string(self):
        return "cassette"
    
    def watch(self, player):
        """Regarde le film"""
        if player.type != "cassette":
            print("Le lecteur n'est pas un lecteur de cassette !")
        else:
            print("Ca commence !")
        super().watch(player)
        
    def rewind (self):
        """On renbobine le film"""
        print("C'est long à rembobiner !")
        self.magnetic_tap = False
        
class Player:
    """Un lecteur"""
    def __init__(self, type):
        self.type = type

type = "cassette"
film = Film("L'odyssé de l'espace")
film_cassette = FilmCassette("Blade runner")

player = Player("DVD")
film_cassette.watch(player)