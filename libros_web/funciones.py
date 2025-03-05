''' Archivo con las fnciones necesarias de la aplicacion libro web '''
import csv

def lee_archivo_csv(archivo:str) -> list:
    ''' Lee un archivo CSV y la convierte e una lista de diccionarios '''
    with open(archivo, 'r', encoding='utf-8') as f:
        return [x for x in csv.DictReader(f)]
    
def crea_diccionario_titulo(lista:list) -> dict:
    ''' Crea un diccionario con los títulos de los libros como llave y el resto de los datos como valor '''
    return {x['title']:x for x in lista}

def busca_en_titulo(diccionario, palabra)->list:
    ''' Busca palabra en titulo de la lista de diccionarios '''
    lista = []
    for titulo, libro in diccionario.items():
        if 'wars' in titulo.lower():
            lista.append(libro)
    return lista

if __name__ == '__main__':
    archivo_csv = 'booklist2000.csv'
    lista_libros = lee_archivo_csv(archivo_csv)
    diccionario_libros = crea_diccionario_titulo(lista_libros)
    resultado = busca_en_titulo(diccionario_libros, 'wars')
    print(resultado)