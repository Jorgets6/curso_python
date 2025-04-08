""" Scrapper para wikipedia """
 
import os
import argparse
import requests
from bs4 import BeautifulSoup
 
def scrap(url:str):
    """ Obtiene página de Internet """
    pagina = requests.get(url,timeout=10)
    if pagina.status_code != 200:
        raise Exception(f"Error {pagina.status_code} en la pagina {url}")
    return pagina
 
def guardar_pagina(pagina,nombre_archivo:str):
    """ Guarda la página en un archivo """
    with open(nombre_archivo, "wb") as f:
        f.write(pagina.content)
    print(f"Pagina guardada en {nombre_archivo}")
 
def main(url:str, archivo_salida:str):
    """ Funcion principal """
    if not os.path.exists(archivo_salida):
        pagina = scrap(url)
        guardar_pagina(pagina, archivo_salida)
    else:
        print(f"El archivo {archivo_salida} ya existe. Leyendo de el.")
        with open(archivo_salida, "rb") as f:
            pagina = f.read()
 
    soup = BeautifulSoup(pagina.content, "html.parser")
    main_content = soup.find("div", class_="mw-body-content")
    if main_content:
        lis_= main_content.find_all("li")
        diccionario_lis = {}
        print(f"Encontré {len(lis_)} elementos <li> en la pagina.")
        for li in lis_[:5]:
            print(f"{li.a.get('href')} : {li.a.text.strip()}")
            diccionario_lis[li.a.text.strip()] = li.a.get("href")
        lista = [{"pelicula":k,"link":v} for k,v in diccionario_lis.items()]
        print(lista)
        archivo_salida = archivo_salida.replace(".html", ".json")
        with open(archivo_salida, "w", encoding="utf-8") as f:
            f.write(str(lista))
       
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Scrapper para Wikipedia")
    parser.add_argument("--url", type=str, help="URL de la pagina a Wikipedia")
    parser.add_argument("--output", type=str, default="wiki.html")
    args = parser.parse_args()
    url = args.url
    output = args.output
    if not url:
        url = "https://es.wikipedia.org/wiki/Anexo:Pel%C3%ADculas_de_ciencia_ficci%C3%B3n#1955"
    if not output:
        output = 'wiki.html'
 
    main(url, output)