'''
Funciones auxiliares para el juego del ahorcado
'''

def carga_archivo_texto(archivo:str)->list:
    '''
    Carga un archivo de textp y devuelve una lista con las otaciones del archivo
    '''
    
    with open(archivo, 'r', encoding='utf-8')as file: oraciones = file.readlines()
    return oraciones

if __name__ == '__main__':
    lista = carga_archivo_texto('./plantillas/plantilla_0.txt')
    for elemento in lista:
        print(elemento)
        
        