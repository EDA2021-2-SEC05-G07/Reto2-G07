"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

#Carga de datos
def iniciarDatos():
    catalog={'Artists': None, 'Artworks': None, 'Medium': None}

    catalog['Artists']= lt.newList()
    catalog['Artworks']= lt.newList()
    catalog['Medium']=mp.newMap(1000, maptype='CHAINING', loadfactor=0.7, comparefunction=None)

    return catalog

def addArtist(catalog, artist):
    lt.addLast(catalog['Artists'], artist)

def addArtwork(catalog, artwork):
    lt.addLast(catalog['Artworks'],artwork)
    for tecnica in catalog['Artworks']['Medium']:
        mp.put(catalog['Medium'],tecnica, artwork)

def ordenar(o1,o2):
    return o1['fecha']<o2['fecha']


def orgObrasCro(catalog, medio):
    obras =lt.newList()
    for obra in lt.iterator(catalog['Artwoks']):
        if medio == obra['Medium']:
            informacion= lt.newList()
            lt.addLast(informacion, obra['Title'])
            lt.addLast(informacion, obra['Date'])
            lt.addLast(obras,informacion)
    return obras

def listaFechas(obras):
    fechas= lt.newList()
    for obra in obras:
        x= obra['Date']
        lt.addLast(fechas, x)
    return fechas 

def ordenarlista(fechas):
    listaOrdenada=sa.sort(fechas, ordenar)
    return listaOrdenada

def topnAntiguas(listaOrdenada, obras, n:int):
    titulosOrdenados= lt.newList()
    for fecha in listaOrdenada:
        for obra in obras:
            if fecha == obra['Date']:
                lt.addLast(titulosOrdenados, obra['Title'])
    posicion= n-1
    topn= lt.subList(titulosOrdenados,lt.size(titulosOrdenados)-posicion,n)
    return topn

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

# Funciones de comparación

def compareMedium(medium1, medium2):
    pass 

