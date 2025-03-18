''' Clases del sistema de peliculas, actores y actrices '''
import csv
from hashlib import sha256
from datetime import datetime



class Actor:
    ''' Clase actor '''
    def __init__(self, id_estrella, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen, username):
        self.id_estrella                = id_estrella
        self.nombre                     = nombre
        self.fecha_nacimiento           = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
        self.ciudad_nacimiento          = ciudad_nacimiento
        self.url_imagen                 = url_imagen
        self.username                   = username

def to_dict(self):
    "Retorna un diccionario con un atributo del objeto"
    return{
        'id_estrella': self.id_estrella,
        'nombre': self.nombre,
        'fecha_nacimiento': self.fecha_nacimiento
    }
