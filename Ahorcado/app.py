'''

'''

import string
import unicodedata
from random import choice
import funciones as fn 

def main(archivo_texto:str, nombre_plantilla="plantilla"):
    '''
    Programa principal del juego del ahorcado
    '''
    # cargamos las plantillas
    plantillas = fn.carga_plantillas(nombre_plantilla)
    # cargamos las oraciones
    oraciones = fn.carga_archivo_texto(archivo_texto)
    #obtenemos las palabras
    palabraas = fn.obten_palabras(oraciones)
    o = 5 # 5 oportunidades para fallar
    p = choice(palabraas) #elegimos una palabra al azaer
    abcedario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o > 0:
        fn.despliega_plantilla(plantillas, o)
        fn.adivina_letra(abcedario, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Felicidades, adivinaste la palabra')
            break
if __name__ == "__main__":
    archivo = './datos/pg15532.txt'
    main(archivo)