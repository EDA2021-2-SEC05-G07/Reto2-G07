"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1 - Cargar información en el catálogo")
    print("2 - Buscar las n obras mas antiguas de un medio")
    print("3 - numero de obras de una nacionalidad")
catalog = None

def initDatos():
    return controller.getiniciarDatos()

def cargarDatos(catalog):
    return controller.cargarDatos(catalog)

def gettopnAntiguas(n:int):
    
    return controller.gettopnAntiguas(listaOrdenada, obras, n)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog= initDatos()
        cargarDatos(catalog)

    elif int(inputs[0]) == 2:
        n= input('Ingrese un numero: ')
        medio= input('Ingrese el medio que quiere buscar: ')
        print('las n obras más antiguas de' + str(medio))
        obras = controller.getorgObrasCro(catalog, medio)
        fechas = controller.getlistaFechas(obras)
        listaOrdenada = controller. getordenarlista(fechas)
        nObras = controller.gettopnAntiguas(listaOrdenada, obras, n)

    elif int(inputs[0]) == 3:
        nacionalidad = input('Ingrese la nacionalidad que quiere buscar: ')
        cant = controller.getSizeNatio(catalog, nacionalidad)
        print('El número total de obras de la nacionalidad'+ str(nacionalidad) + 'es: ' + str(cant))
        

    else:
        sys.exit(0)
sys.exit(0)
