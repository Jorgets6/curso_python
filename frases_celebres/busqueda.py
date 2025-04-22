import csv
import os

def lee_archivo_csv(archivo: str) -> list:
    ''' Lee el archivo CSV sin encabezados y lo convierte en una lista de diccionarios '''
    with open(archivo, "r", encoding='utf8') as f:
        return [{'frase': row[0], 'autor': row[1]} for row in csv.reader(f)]
    
def crea_diccionario(lista: list) -> dict:
    ''' Crea un diccionario con índices numéricos como claves '''
    return {i: item for i, item in enumerate(lista)}

def buscar_frases(diccionario: dict, palabras: list) -> list:
    ''' Busca frases que contengan una o varias palabras '''
    resultados = []
    for _, valores in diccionario.items():
        frase = valores.get('frase', '').lower()
        if all(palabra.lower() in frase for palabra in palabras):
            resultados.append(valores)
    return resultados

def main():
    archivo = "frases.csv" 
    if not os.path.exists(archivo):
        print(f"El archivo {archivo} no existe.")
        return

    lista = lee_archivo_csv(archivo)
    diccionario = crea_diccionario(lista)

    print("Introduce las palabras clave para buscar (separadas por espacios):")
    palabras = input().strip().split()

    resultados = buscar_frases(diccionario, palabras)
    if resultados:
        print("\nResultados encontrados:")
        for resultado in resultados:
            print(f"Frase: {resultado.get('frase', 'N/A')}")
            print(f"Película/Fuente: {resultado.get('autor', 'N/A')}")
            print("-" * 60)
    else:
        print("\nNo se encontraron resultados.")

if __name__ == "__main__":
    main()