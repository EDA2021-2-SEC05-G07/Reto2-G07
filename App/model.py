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


from DISClib.DataStructures.arraylist import newList
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
                                 comparefunction=compareMedium)
    catalog['Nationality']=mp.newMap(1153,
                                    maptype='PROBING',
                                    loadfactor=0.6,
                                    comparefunction=compareNationality)
    catalog['RangoFechasArtistas']=mp.newMap(1153,
                                            maptype='PROBING',
                                            loadfactor=0.6,
                                            comparefunction=compareBeginDate)
    catalog['RangoFechasObras']=mp.newMap(1153,
                                        maptype='PROBING',
                                        loadfactor=0.6,
                                        comparefunction=compareBeginDateObras)
    catalog['Departamento']=mp.newMap(1153,
                                    maptype='PROBING',
                                    loadfactor=0.6,
                                    comparefunction=compareDepartamento)
    catalog['CostoObras']=mp.newMap(1153,
                                    maptype='PROBING',
                                    loadfactor=0.6,
                                    comparefunction=compareCostoObras)
    return catalog

def addArtist(catalog, artist):
    lt.addLast(catalog['Artists'], artist)
    fechabegin= artist['BeginDate']
    esta = mp.contains(catalog['RangoFechasArtistas'], fechabegin)
    if not esta:
        listaArtista = lt.newList()
        lt.addLast(listaArtista, artist)
        mp.put(catalog['RangoFechasArtistas'], fechabegin, listaArtista)
    else:
        listaArtista = mp.get(catalog['RangoFechasArtistas'], fechabegin)['value']
        lt.addLast(listaArtista, artist)
        mp.put(catalog['RangoFechasArtistas'], fechabegin, listaArtista)

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
    i = True
    while inicial <= final and i== True:
        esta = mp.contains(catalog['RangoFechasArtistas'], inicial)
        if esta: 
            lista = mp.get(catalog['RangoFechasArtistas'], inicial)['value']
            for element in lt.iterator(lista):
                lt.addLast(listaArtistas, element)
            for artista in listaArtistas:
                listaInfo= lt.newList()
                lt.addLast(listaInfo, artista['DisplayName'])
                lt.addLast(listaInfo, artista['BeginDate'])
                lt.addLast(listaInfo, artista['EndDate'])
                lt.addLast(listaInfo, artista['Nationality'])
                lt.addLast(listaInfo, artista['Gender'])
                i = False
    return listaInfo
def listafechas(listaInfo):
    for artista in listaInfo:
        listaFechas= lt.newList()
        lt.addLast(listaFechas, artista['BeginDate'])
    return listaFechas
    
def ordenar(o1,o2):
    return o1['fecha']<o2['fecha']
def ordenarlista(listafechas):
    listaOrdenada=sa.sort(listafechas, ordenar)
    return listaOrdenada
def ordenarArtistas(listainfo):
    ordenada= ordenarlista(listainfo)
    return ordenada
def primeros3(ordenada):
    primeros=lt.subList(ordenada, 1, 3)
    return primeros
def ultimos3(ordenada):
    ultimos=lt.subList(ordenada, (lt.size(ordenada))-2, 3)
    return ultimos

#falta ordenar la lista para poder sacar los primeros y ultimos 3

#Requerimiento 2
def compararIDayo(catalog, id):
    #en id entraria el constituent ID del artworks
    for artist in lt.iterator(catalog['Artist']):
        if id == artist['ConstituentID']:
            nomArtista = artist['DisplayName']
            return nomArtista

def orgObrasCro(catalog, inicial, final):
    for obra in lt.iterator(catalog['Artworks']):        
        if obra['DateAcquired']>= inicial and obra['DateAcquired']<= final:
            informacion= lt.newList()
            lt.addLast(informacion, obra['Title'])
            lt.addLast(informacion, obra[compararIDayo(obra['ConstituentID'])])
            lt.addLast(informacion, obra['Date'])
            lt.addLast(informacion, obra['DateAcquired'])
            lt.addLast(informacion, obra['Medium'])
            lt.addLast(informacion, obra['Dimensions'])
            mp.put(catalog['RangoFechasObras'],obra['Title'], informacion)
    conteoObras=lt.size(catalog['RangoFechasObras'])
    return conteoObras

def ordenarObras(obras):
    ordenada= ordenarlista(obras)
    return ordenada

def numPurchase(catalog):
    conteoPu = 0
    for obra in lt.iterator(catalog['Artworks']):
        if obra['CreditLine'] == 'Purchase':
            conteoPu += 1
        return conteoPu

def ordenarArtistas(artistas):
    ordenada= ordenarlista(artistas)
    return ordenada

def orgObrasCro(catalog, medio):
    obras =lt.newList()
    for obra in lt.iterator(catalog['Artworks']):
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

#Requerimiento 3

def enconID(catalog, nombre):
    i=0
    f=len(catalog['Artists'])
    f-=1
    pos=-1
    id= False
    while i <= f and id == False:
        m=(i+f)//2
        if catalog['Artists'][m]== nombre:
            pos=m
            id=True
        elif catalog['Artists'][m] > nombre:
            f=m-1
        else:
            i=m+1
    encontrarid= catalog['Artists'][pos]['Constituent ID']
    return encontrarid
def tecnicasartista(catalog, encontrarid):
    cantidadobras=0
    tecnicas=lt.newList()
    listastecnicas=lt.newList()
    for obra in lt.iterator(catalog['Artworks']):
        if obra['Constituent ID'] == encontrarid:
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

def ordenar(o1,o2):
    return o1['fecha']<o2['fecha']

def ordenarlista(listafechas):
    listaOrdenada=sa.sort(listafechas, ordenar)
    return listaOrdenada

def listaprecios(catalog):
    listaprecios= lt.newList('SINGLE_LINKED')
    obra= mp.keySet(catalog['CostoObras'])
    parejaObra = mp.get(catalog['Departamento'], obra)
    for llave in parejaObra:
        costo= catalog['CostoObras'][llave]
        lt.addLast(listafechas, {'costo': costo, 'titulo': llave})
    return listaprecios

def ordenar2(o1,o2):
    return o1['costo']<o2['costo']

def ordenarlista2(listaprecios):
    listaOrdenadaprecios2=sa.sort(listaprecios, ordenar)
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

def obrasMasCost(listaOrdenadaprecios2, catalog, lista):
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
    ####################

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
    medium2= me.getKey(medium2)
    if (medium1) == (medium2):
        return 0
    elif (medium1) > (medium2):
        return 1
    else:
        return -1
def compareNationality(natio1, natio2):
    natio2= me.getKey(natio2)
    if (natio1) == (natio2):
        return 0
    elif (natio1) > (natio2):
        return 1
    else:
        return -1
def compareBeginDate(date1, date2):
    date2= me.getKey(date2)
    if (date1) == (date2):
        return 0
    elif (date1) > (date2):
        return 1
    else:
        return -1
def compareEndDate(date1, date2):
    date2= me.getKey(date2)
    if (date1) == (date2):
        return 0
    elif (date1) > (date2):
        return 1
    else:
        return -1
def compareBeginDateObras(date1, date2):
    date2= me.getKey(date2)
    if (date1) == (date2):
        return 0
    elif (date1) > (date2):
        return 1
    else:
        return -1
def compareDepartamento(dep1, dep2):
    dep2= me.getKey(dep2)
    if (dep1) == (dep2):
        return 0
    elif (dep1) > (dep2):
        return 1
    else:
        return -1
def compareCostoObras(cos1, cos2):
    cos2= me.getKey(cos2)
    if (cos1) == (cos2):
        return 0
    elif (cos1) > (cos2):
        return 1
    else:
        return -1



def compareTecnicas(tec1, tec2):
    tec2= me.getKey(tec2)
    if (tec1) == (tec2):
        return 0
    elif (tec1) > (tec2):
        return 1
    else:
        return -1