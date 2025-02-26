'''
Con un vasito en la mano 
El cuerpo siento cansado
Fumando voy relajado
'''

from random import choice
from Athlete import Athlete
from Sport import Sport
from team import Team
import json

class Game:
    ''' Clase Game: Juego entre dos equipos'''
    sports_dict = {
            'LMP': [x for x in range(0, 11)],
            'NBA': [x for x in range(50, 150)],
            'NFL': [x for x in range(0, 20)],
            'MLX': [x for x in range(0, 10)],
            'FIFA': [x for x in range(0, 10)]
        }
    def __init__(self, A: True, B: True):
        ''' Constructor de la clase'''
        self.A = A
        self.B = B                           
        self.score = dict()
        self.score[A.name] = 0
        self.score[B.name] = 0
        
    def play(self):
        ''' Juego simulado entre dos equipos '''
        league = self.A.sport.league
        points = self.sports_dict[league]
        a = choice(points)
        b = choice(points)
        self.score[self.A.name] = a
        self.score[self.B.name] = b 
        
        
    def __str__(self):
        ''' Metodo para representar la clase como string'''
        return f"Game: {self.A.name}: {self.score[self.A.name]} - {self.score[self.B.name]}: {self.B.name}"
    
    def __repr__(self):
        ''' Metodo para representar la clase como string'''
        return f"Game(A={repr(self.A)}, B={repr(self.B)}, score={self.score})"
    
    def to_json(self) -> dict:
        ''' Metodo para convertir la clase en un diccionario'''
        return {"A": self.A.to_json(), "B": self.B.to_json(), "score": self.score}
        
                
if __name__ == "__main__":
    dt = ['Jordan', 'Jhonson', 'Pipen', 'Bird', 'Kobe']
    c2 = ['Bjovik', 'Czack', 'Pfeizer', 'Leonard', 'Kempfe']
    players_a = [Athlete(x) for x in dt]
    players_b = [Athlete(x) for x in c2]
    basketball = Sport('Basketball', 5, 'NBA')
    team_a = Team("Dream Team", basketball, players_a)
    team_b = Team("Czeck Republic", basketball, players_b)
    game = Game(team_a, team_b)
    print(game)
    game.play()
    print(game)
    print("-------------------")
    print(repr(game))
    print(game.to_json())
    filename_json = "game.json"
    with open(filename_json, "w", encoding='utf8') as f:
        json.dump(game.to_json(), f, ensure_ascii=False, indent=4)
    print(f"Archivo{filename_json} guardado con éxito!")
    
    
    
    