# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso <2022>/<2023>)
Autor/a: Tomás cruz Ferrer  uvus:BFS3928

Trata sobre un estudio del contenido de netflix en el cual se identifican suiguientes datos como: type, title, director, country, co_production, date_added, release_year, duration, description.

# Estructura de las carpetas del proyecto
/src: Contiene los diferentes módulos de Python que conforman el proyecto.
<plataforma.py>:Es un archivo en el cual se definen las funciones
<plataforma_test.py>: Es el archivo en el que ejecuto las funciones definidas
/data: Contiene el dataset o datasets del proyecto
<plataforma_streaming.py> : Archivo csv que se quiere leer
<parsers.py>: Es un archivo que contiene el parse de datetime
# Estructura del dataset:
Tiene un encabezado con distintos campos.

El dataset está compuesto por 9 columnas, con la siguiente descripción:

type: de tipo string, el tipo de contenido
title: de tipo string, representa el nombre del contenido
director: de tipo string, representa el director del contenido
country: de tipo string, representa el lugar donde se produjo
co_production: de tipo string, representa el nombre de la productora
date_added: de tipo datetime, representa la fecha que salió en la plataforma
release_year: de tipo int, representae l año en el que se estrenó
duration: de tipo int, representa la duración del contenido
description: de tipo string, representa una breve introducción del contenido


# Tipos implementados

He usado un namedtuple para dividir el archivo por columnas y a esas columnas las he llamado: type, title, director, country, co_production, date_added, release_year, duration, description.

# Funciones implementadas
"lee_datos_fichero" es una función que abre, lee y cierra un archivo csv de tal forma que lo estructura por columnas, transforma las columnas de tipo y añade todo el contendio del csv a una lista que nos devuelve después. Por predeterminado los valores nos lo devuelve en string, pero si queremos pasarla a datetime tenemos que parsearla, y para eso he creado otra función llamada "parse_fecha" que la he puesto en otro archivo para que pueda reutilizarla en otro momento.

En "plataforma_test" he invocado a la función "lee_datos_fichero" para que me lea el csv