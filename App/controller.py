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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def getiniciarDatos():
    catalog= model.iniciarDatos()
    return catalog

catalog= getiniciarDatos()

def cargarDatos(catalog):

    loadArtist(catalog)
    loadArtworks(catalog)
    model.cargarmapaMedios(catalog)
    model.cargarNacionalidades(catalog)

def loadArtist(catalog):
    artistfile= cf.data_dir + 'Artists-utf8-small.csv'
    input_file= csv.DictReader(open(artistfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtworks(catalog):
    artworksfile= cf.data_dir + 'Artworks-utf8-small.csv'
    input_file= csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

def getordenar(o1,o2):
    resultado= model.ordenar(o1,o2)
    return resultado

def getorgObrasCro(catalog, medio):
    obras= model.orgObrasCro(catalog, medio)
    return obras


def getlistaFechas(obras):
    fechas= model.listaFechas(obras)
    return fechas


def getordenarlista(fechas):
    listaOrdenada= model.ordenarlista(fechas)
    return listaOrdenada


def gettopnAntiguas(listaOrdenada, obras, n:int):
    topn= model.topnAntiguas(listaOrdenada, obras, n)
    return topn

def getSizeNatio(catalog, nacionalidad):
    size = model.sizeNatio(catalog, nacionalidad)
    return size

#Requerimiento 1
def getorgartistasCro(catalog, inicial, final):
    size= model.orgartistasCro(catalog, inicial, final)
    return size
#Requerimiento 2
def getorgObrasCro(catalog, inicial, final):
    conteoObras= model.orgObrasCro(catalog, inicial, final)
    return conteoObras
def getcompararIDayo(catalog, id):
    nomArtista= model.compararIDayo(catalog, id)
    return nomArtista
def getordenarObras(obras):
    ordenada= model.ordenarObras(obras)
    return ordenada
def getnumPurchase(catalog):
    conteoPu= model.numPurchase(catalog)
    return conteoPu
    
# Funciones requerimiento 4
def getidArtists(catalog):
    id=model.idArtists(catalog)
    return id
def getidyNacio(catalog, id):
    "que retorna ?"
    return model.idyNacio(catalog, id)
def getcontNacio(catalog):
    conteoNa = model.contNacio(catalog)
    return conteoNa
def getTop10(catalog):
    top10= model.Top10(catalog)
    return top10
def getnacioMasObras(top10, catalog):
    obrasNa= model.nacioMasObras(top10, catalog)
    return obrasNa
def getlista_nacionalidades(catalog):
    lst_top10_final=model.lista_nacionalidades(catalog)
    return lst_top10_final

#Requerimiento 5
def getlistafechas(catalog):
    listafechas= model.listafechas(catalog)
    return listafechas
def getordenar(o1,o2):
    orden=model.ordenar(o1,o2)
    return orden
def getordenarlista(listafechas):
    listaordenada=model.ordenarlista(listafechas)
    return listaordenada
def getlistaprecios(catalog):
    listaprecios= model.listaprecios(catalog)
    return listaprecios
def getordenar(o1,o2):
    orden2= model.ordenar2(o1,o2)
    return orden2
def getordenarlista(listafechas):
    listaOrdenadaprecios2= model.ordenarlista(listafechas)
    return listaOrdenadaprecios2
def getordenar2(o1,o2):
    resultado= model.ordenar2(o1,o2)
    return resultado
def getordenarlista2(listaprecios):
    listaOrdenadaprecios2= model.ordenarlista2(listaprecios)
    return listaOrdenadaprecios2
def getpesototal(catalog):
    peso= model.pesototal(catalog)
    return peso
def getcantidadObras(catalog):
    totalObras= model.cantidadObras(catalog)
    return totalObras
def getcostoEstimado(catalog):
    suma= model.costoEstimado(catalog)
    return suma
def getobrasMasAntiguas(listaOrdenada, catalog):
    masAntiguas= model.obrasMasAntiguas(listaOrdenada, catalog)
    return masAntiguas
def getobrasMasCost(listaOrdenadaprecios2, catalog):
    masCost= model.obrasMasCost(listaOrdenadaprecios2, catalog)
    return masCost
# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
