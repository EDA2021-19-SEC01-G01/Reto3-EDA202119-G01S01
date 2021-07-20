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
from DISClib.ADT import map as mp
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Requerimiento 1")
    print("3- Requerimiento 2")
    print("4- Requerimiento 3")
    print("5- Requerimiento 4")
    print("0- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.init()
        catalog = controller.loadData(catalog,'context_content_features-small.csv')
        tamano = lt.size(catalog['events'])
        tamanoArt = mp.size(catalog["artistas"])
        tamanoSongs = mp.size(catalog["songs"])
        print(f"La cantidad de eventos cargados es: {tamano}")
        print(f"La cantidad de artistas cargados es: {tamanoArt}")
        print(f"La cantidad de canciones cargadas es: {tamanoSongs}")
        parteIni = lt.subList(catalog['events'],1,5)
        for i in range(1,6):
            print(lt.getElement(parteIni,i))
        parteEnd = lt.subList(catalog['events'],tamano-5,5)
        for i in range(1,6):
            print(lt.getElement(parteEnd,i))

    elif int(inputs[0]) == 2:
        crit1 = input("Ingrese el criterio 1: ")
        minimo1 = float(input("Ingrese el mínimo 1: "))
        maximo1 = float(input("Ingrese el máximo 1: "))
        crit2 = input("Ingrese el criterio 2: ")
        minimo2 = float(input("Ingrese el mínimo 2: "))
        maximo2 = float(input("Ingrese el máximo 2: "))
        rta = controller.requerimiento1(catalog,crit1,minimo1,maximo1,crit2,minimo2,maximo2)
        print (f"Número de eventos dentro de ambos rangos: {rta[0]}")
        print (f"Número de artistas con reproducciones dentro de ambos rangos: {rta[1]}")

    else:
        sys.exit(0)
sys.exit(0)
