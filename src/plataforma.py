from collections import namedtuple
import csv
from parsers import * #importa todas las bibliotecas de parsers

contenido = namedtuple("contenido","type,title,director,country,co_production,date_added,release_year,duration,description")
#type;title;director;country;co_production;date_added;release_year;duration;description
def lee_datos_fichero(path):#direccion del archivo
    with open(path, mode="rt", encoding="utf-8",)as f:

        lector=csv.reader(f,delimiter=";")
        next(lector)

        lista=[]#Lista que se rellena con los archivos del csv

        for type,title,director,country,co_production,date_added,release_year,duration,description in lector:
            #parsers:
            duration = int(duration) #parsers
            date_added=parse_fecha(date_added)
            release_year=int(release_year)

            t=contenido(type,title,director,country,co_production,date_added,release_year,duration,description)
            print(t)
            lista.append(t)#variable que guarda una linea completa y almacena en contenido
        return lista  
        




