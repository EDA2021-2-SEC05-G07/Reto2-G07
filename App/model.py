﻿"""
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


from DISClib.DataStructures.arraylist import addLast, newList
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
    catalog={'Artists': None,
            'Artworks': None,
            'Medium': None,
            'Nationality': None,
            'RangoFechasArtistas': None,
            'RangoFechasObras': None,
            'Departamento': None}

    catalog['Artists']= lt.newList()
    catalog['Artworks']= lt.newList()
    catalog['Medium']=mp.newMap(1153,
                                 maptype='PROBING',
                                 loadfactor=0.6,
                                 comparefunction=compareVariables)
    catalog['Nationality']=mp.newMap(1153,
                                    maptype='PROBING',
                                    loadfactor=0.6,
                                    comparefunction=compareVariables)
    catalog['RangoFechasArtistas']=mp.newMap(1153,
                                            maptype='PROBING',
                                            loadfactor=0.6,
                                            comparefunction=compareVariables)
    catalog['RangoFechasObras']=mp.newMap(1153,
                                        maptype='PROBING',
                                        loadfactor=0.6,
                                        comparefunction=compareVariables)
    catalog['Departamento']=mp.newMap(1153,
                                    maptype='PROBING',
                                    loadfactor=0.6,
                                    comparefunction=compareVariables)
    catalog['CostoObras']=mp.newMap(1153,
                                    maptype='PROBING',
                                    loadfactor=0.6,
                                    comparefunction=compareVariables)
    return catalog

def addArtist(catalog, artist):
    lt.addLast(catalog['Artists'], artist)
    nombre = artist['DisplayName']
    esta = mp.contains(catalog['RangoFechasArtistas'], nombre)
    if not esta:
        listaArtista = lt.newList()
        lt.addLast(listaArtista, artist)
        mp.put(catalog['RangoFechasArtistas'], nombre, listaArtista)
    else:
        listaArtista = mp.get(catalog['RangoFechasArtistas'], nombre)['value']
        lt.addLast(listaArtista, artist)
        mp.put(catalog['RangoFechasArtistas'], nombre, listaArtista)

def cargarmapaMedios(catalog):
    for obra in lt.iterator(catalog['Artworks']):
        if mp.contains(catalog['Medium'],obra['Medium']):
            valor=mp.get(catalog['Medium'], obra['Medium'])
            value= me.getValue(valor)
            lt.addLast(value, obra)
        else:
            lista= lt.newList()
            lt.addLast(lista, obra)
            mp.put(catalog['Medium'],obra['Medium'], lista)
def cargarNacionalidades(catalog):
    for artista in lt.iterator(catalog['Artists']):
        id= artista['ConstituentID']
        listaObras= lt.newList()
        for obra in lt.iterator(catalog['Artworks']):
            if id == obra['ObjectID']:
                lt.addLast(listaObras, obra)

        if mp.contains(catalog['Nationality'],artista['Nationality']):
            valor=mp.get(catalog['Nationality'], artista['Nationality'])
            value= me.getValue(valor)
            for obra in lt.iterator(listaObras):
                lt.addLast(value, obra)
        else:
            mp.put(catalog['Nationality'],artista['Nationality'], listaObras)

def addArtwork(catalog, artwork):
    lt.addLast(catalog['Artworks'],artwork)
    obra = artwork['Title']
    esta = mp.contains(catalog['RangoFechasObras'], obra)
    if not esta:
        listaObra = lt.newList()
        lt.addLast(listaObra, obra)
        mp.put(catalog['RangoFechasObras'], obra, listaObra)
    else:
        listaObra = mp.get(catalog['RangoFechasObras'], obra)['value']
        lt.addLast(listaObra, obra)
        mp.put(catalog['RangoFechasObras'], obra, listaObra)

def sizeNatio(catalog, nacionalidad):
    contador = 0
    for obra in lt.iterator(catalog['Artworks']):
        if obra['Nationality'] == nacionalidad:
            contador+=1 
    return contador

def ordenar(o1,o2):
    return o1['fecha']<o2['fecha']

#Requerimiento 1

def orgartistasCro(catalog, inicial, final):
    listaArtistas = lt.newList()
    valores = mp.valueSet(catalog['RangoFechasArtistas'])
    for artista in valores:
        if artista['BeginDate']>=inicial and artista['BeginDate']<= final:
            listaInfo= lt.newList()
            lt.addLast(listaInfo, artista['DisplayName'])
            lt.addLast(listaInfo, artista['BeginDate'])
            lt.addLast(listaInfo, artista['EndDate'])
            lt.addLast(listaInfo, artista['Nationality'])
            lt.addLast(listaInfo, artista['Gender'])
            lt.addLast(listaArtistas, listaInfo)       
    total = lt.size(listaArtistas)   
    return (total, listaArtistas)

def listafechas(listaArtistas):
    listaFechas= lt.newList()
    for artista in listaArtistas:
        lt.addLast(listaFechas, artista['BeginDate'])
    return listaFechas

def ordenarlista(listafechas):
    listaOrdenada=sa.sort(listafechas, compareVariables)
    return listaOrdenada
def ordenarArtistas(listaOrdenada, listaArtistas):
    ordenada = lt.newList
    for fecha in listaOrdenada:
        for artista in listaArtistas:
            if fecha == artista['BeginDate']:
                lt.addLast(ordenada, artista)
    return ordenada
def primeros3(ordenada):
    primeros=lt.subList(ordenada, 1, 3)
    return primeros
def ultimos3(ordenada):
    ultimos=lt.subList(ordenada, (lt.size(ordenada))-2, 3)
    return ultimos

#Requerimiento 2
def compararIDayo(catalog, id):
    #en id entraria el constituent ID del artworks
    for artist in lt.iterator(catalog['Artist']):
        if id == artist['ConstituentID']:
            nomArtista = artist['DisplayName']
    return nomArtista

def orgObrasCro(catalog, inicial, final):
    listaObras= lt.newList()
    valores = mp.valueSet(catalog['RangoFechasObras'])
    for obra in valores:        
        if obra['DateAcquired']>= inicial and obra['DateAcquired']<= final:
            informacion= lt.newList()
            lt.addLast(informacion, obra['Title'])
            lt.addLast(informacion, obra[compararIDayo(catalog['Artist'],obra['ConstituentID'])])
            lt.addLast(informacion, obra['Date'])
            lt.addLast(informacion, obra['DateAcquired'])
            lt.addLast(informacion, obra['Medium'])
            lt.addLast(informacion, obra['Dimensions'])
            lt.addLast(listaObras, informacion)
    conteoObras=lt.size(listaObras)
    return (conteoObras, listaObras)

def listafechasObras(listaObras):
    listafechas = lt.newList()
    for obra in listaObras:
        lt.addLast(listafechas, obra['DateAcquired'])
    return listafechas

def ordenarObras(listaOrdenada, listaObras):
    ordenada = lt.newList
    for fecha in listaOrdenada:
        for obra in listaObras:
            if fecha == obra['DateAcquired']:
                lt.addLast(ordenada, obra)
    return ordenada

def numPurchase(catalog):
    conteoPu = 0
    for obra in lt.iterator(catalog['Artworks']):
        if obra['CreditLine'] == 'Purchase':
            conteoPu += 1
    return conteoPu

#Requerimiento 3

def enconID(catalog, nombre: str):
    encontrarid=None
    for artista in lt.iterator(catalog['Artists']):
        if artista['DisplayName']== nombre:
            encontrarid= artista['ConstituentID']
            break
    return encontrarid
def tecnicasartista(catalog, encontrarid):
    cantidadobras=0
    tecnicas=lt.newList()
    for obra in lt.iterator(catalog['Artworks']):
        if obra['ConstituentID'] == encontrarid:
            cantidadobras+=1
            tecnica2= obra['Medium']
            if tecnica2 in tecnicas:
                nuevaObra=lt.newList()
                lt.addLast(nuevaObra,obra['Title'])
                lt.addLast(nuevaObra,obra['Date'])
                lt.addLast(nuevaObra,obra['Medium'])
                lt.addLast(nuevaObra,obra['Dimensions'])
                lt.addLast(tecnica2,nuevaObra)
            else:
                lt.addLast(tecnicas, tecnica2)
                tecnica2=lt.newList()
                nuevaObra=lt.newList()
                lt.addLast(nuevaObra,obra['Title'])
                lt.addLast(nuevaObra,obra['Date'])
                lt.addLast(nuevaObra,obra['Medium'])
                lt.addLast(nuevaObra,obra['Dimensions'])
                lt.addLast(tecnica2,nuevaObra)
    mayor=0
    masgrande=None
    for tec in tecnicas:
        tamanio= lt.size(tec)
        if tamanio > mayor:
            mayor= tamanio
            masgrande=tec
    tecnicas= lt.size(tecnicas)
    tupla=(cantidadobras, tecnicas, masgrande)
    return tupla

#Requerimiento 4
def idArtists(catalog):
    for artist in lt.iterator(catalog['Artists']):
        id = artist['ConstituentID']
    return id

def idyNacio(catalog, id):
    #en id entraria el constituent ID de artists (return idArtists)
    for obra in lt.iterator(catalog['Artworks']):
        if id == obra['ConstituentID']:
            for artista in lt.iterator(catalog['Artists']):
                nacionalidad = artista['Nationality']
                mp.put(catalog['Nationality'], nacionalidad, '')

def contNacio(catalog):
    conteoNa = 0
    for artist in lt.iterator(catalog['Artists']):
        nacionalidad = artist['Nationality']
        natioKeys = mp.keySet(catalog['Nationality'])
        if nacionalidad in natioKeys:
            conteoNa += 1
            mp.put(catalog['Nationality'], nacionalidad, conteoNa)
            return conteoNa
    
def Top10(catalog):
    valoresNacio=lt.newList()
    top10=  lt.newList()
    indice = mp.keySet(catalog['Nationality'])
    pareja = mp.get(catalog['Nationality'], indice)
    for nacio in pareja:
        lt.addLast(valoresNacio, nacio)
    valoresOrdenados= sa.sort(valoresNacio)
    valorestop10= lt.subList(valoresOrdenados, 1, 10)
    for valor in lt.iterator(valorestop10):
        natioKeys = mp.keySet(catalog['Nationality'])
        for valornacionalidad in natioKeys:
            if natioKeys[valornacionalidad] == valor:
                nacionalidad= valornacionalidad
                lt.addLast(top10, nacionalidad)
    return top10

def nacioMasObras(top10, catalog):
    uno = lt.getElement(top10,1)
    for artista in lt.iterator(catalog['Artists']):
        nacionalidad = artista['Nationality']
        if nacionalidad == uno:
            id= artista['ConstituentID']
            for obra in lt.iterator(catalog['Artworks']):
                if id == obra['ConstituentID']:
                    for obra in top10:
                        x = lt.newList
                        lt.addLast(x, obra['Title'])
                        lt.addLast(x, obra['Date'])
                        lt.addLast(x, obra['Medium'])
                        lt.addLast(x, obra['Dimensions'])
                        lt.addLast(x, obra[compararIDayo(obra['ConstituentID'])])
                        obrasNa = lt.newList
                        lt.addLast(obrasNa,x)
    return obrasNa

def lista_nacionalidades(catalog):
    mayor=0
    top10= 0
    lst_nacio_ord = lt.newList
    natio= mp.keySet(catalog['Nationality'])
    parejaNatio= mp.get(catalog['Nationality'], natio)
    for obra in parejaNatio:
        size= lt.size(obra)
        if size > mayor:
            mayor= size
            while top10 <= 10:
                key = mp.valueSet(catalog['Nationality'])
                if key == natio['Nationality']:
                    nacionalidad_mas_repetida = key
                    top10+= 1
                    lst_top10_final = lt.addLast(lst_nacio_ord,nacionalidad_mas_repetida)
    return lst_top10_final

#Requerimiento 5
def obrasDepartamento(departamento, catalog):
    for obra in lt.iterator(catalog['Artworks']):
        if catalog['Artworks']['Department'] == departamento:
            mp.put(catalog['Departamento'],obra['Title'], obra)
def listafechas(catalog):
    listafechas= lt.newList('SINGLE_LINKED')
    dep= mp.keySet(catalog['Departamento'])
    parejaDep = mp.get(catalog['Departamento'], dep)
    for obra in parejaDep:
        f= obra['Date']
        t= obra['Title']
        lt.addLast(listafechas, {'fecha': f, 'titulo': t})
    return listafechas

def ordenarlista(listafechas):
    listaOrdenada=sa.sort(listafechas, compareVariables)
    return listaOrdenada

def listaprecios(catalog):
    listaprecios= lt.newList('SINGLE_LINKED')
    obra= mp.keySet(catalog['CostoObras'])
    parejaObra = mp.get(catalog['Departamento'], obra)
    for llave in parejaObra:
        costo= catalog['CostoObras'][llave]
        lt.addLast(listafechas, {'costo': costo, 'titulo': llave})
    return listaprecios

def ordenarlista2(listaprecios):
    listaOrdenadaprecios2=sa.sort(listaprecios, compareVariables)
    return listaOrdenadaprecios2

def pesototal(catalog):
    peso=0
    dep= mp.keySet(catalog['Departamento'])
    parejaDep = mp.get(catalog['Departamento'], dep)
    for obra in parejaDep:
        pesoObra= int(obra['Weight'])
        peso+= pesoObra
    return peso

def cantidadObras(catalog):
    totalObras= mp.size(catalog['Departamento'])
    return totalObras

def dictCostos(catalog):
    dep= mp.keySet(catalog['Departamento'])
    parejaDep = mp.get(catalog['Departamento'], dep)
    for obra in parejaDep:
        altura=obra['Height']
        longitud=obra['Length']
        peso=obra['Weigth']
        ancho= obra['Width']
        if (altura== '' or longitud=='') and peso=='':
            mp.put(catalog['CostoObras'],obra['Title'], 48)
        else:
            mayor=0
            costos=lt.newList()
            if longitud != '' and altura!= '':
                area= (altura*longitud)/100
                precioArea= 72/area
                lt.addLast(costos, precioArea)
                if ancho!='':
                    volumen= (altura*longitud*ancho)/100
                    precioVolumen= 72/volumen
                    lt.addLast(costos, precioVolumen)
            if peso != '':
                precioPeso= 72/peso
                lt.addLast(costos, precioPeso)
            for precio in lt.iterator(costos):
                if precio> mayor:
                    mayor= precio
            mp.put(catalog['CostoObras'],obra['Title'], mayor)

def costoEstimado(catalog):
    valores=catalog['CostoObras']
    val= mp.valueSet(valores)
    suma=sum(val)
    return suma

def obrasMasAntiguas(listaOrdenada, catalog):
    x= lt.subList(listaOrdenada, (lt.size(listaOrdenada))-4, 5)
    masAntiguas= lt.newList()
    for obra in lt.iterator(x):
        info= lt.newList()
        lt.addLast(info, obra['Title'])
        id= obra['ConstituentID']
        artista = compararIDayo(catalog,id)
        lt.addLast(info, artista)
        lt.addLast(info, obra['Classification'])
        lt.addLast(info, obra['Date'])
        lt.addLast(info, obra['Medium'])
        lt.addLast(info, obra['Dimensions'])
        costotransporte= dictCostos(catalog)
        for llave in catalog:
            if llave == obra['Title']:
                costo=costotransporte[llave]
                break
        lt.addLast(info, costo)
        lt.addLast(masAntiguas, info)
    return masAntiguas 

def obrasMasCost(listaOrdenadaprecios2, catalog):
    x= lt.subList(listaOrdenadaprecios2, (lt.size(listaOrdenadaprecios2))-4, 5)
    masCost= lt.newList()
    for obra in lt.iterator(x):
        info= lt.newList()
        lt.addLast(info, obra['Title'])
        id= obra['ConstituentID']
        artista = compararIDayo(catalog, id)
        lt.addLast(info, artista)
        lt.addLast(info, obra['Classification'])
        lt.addLast(info, obra['Date'])
        lt.addLast(info, obra['Medium'])
        lt.addLast(info, obra['Dimensions'])
        for llave in catalog['Departamento']:
            if llave == obra['Title']:
                costo=catalog['Departamento'][llave]
                break
        lt.addLast(info, costo)
        lt.addLast(masCost, info)
    return masCost

# Funciones de comparación

def compareVariables(var1, pareja2):
    pareja2= me.getKey(pareja2)
    if (var1) == (pareja2):
        return 0
    elif (var1) > (pareja2):
        return 1
    else:
        return -1