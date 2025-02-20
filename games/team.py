"""
Clase Team: Equipo
"""
from Athlete import Athlete
from Sport import Sport
class Team:
    """Clase para representar un equipo"""
    def __init__(self, name:str, sport: Sport, players:list):
        self.name = name
        self.sport = sport
        self.players = players
        
    def __str__(self):
        """Metodo para reprensentar la clase como string"""
        return f"Team: {self.name}, {self.sport}, {self.players}"
    
    def __repr__(self):
        """ Metodo para represntar la case como string """
        return f"Team(name='{self.name}', sport={self.sport}, players = {self.players})"    
    
    def to_json(self) -> dict:
        """ Metodo para convertir la clase en un diccionario """
        return { "name": self.name, "sport": self.sport.to_json(), "players": [p.to_json() for p in self.players]}
    
if __name__ == "__main__":
    a1 = Athlete("Michael Jordan")
    a2 = Athlete("Lebron James")
    a3 = Athlete("Stephen Curry")
    a4 = Athlete("Shaquille O'Neal")
    a5 = Athlete("Kobe Bryant")
    s = Sport("Basketball", 5, "NBA")
    lakers = Team("Los Angeles Lakers", s, [a1, a2, a3, a4, a5])
    print(lakers)
    print(repr(lakers))
    print(lakers.to_json())
    