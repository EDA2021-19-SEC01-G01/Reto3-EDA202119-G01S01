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
from DISClib.ADT import orderedmap as om
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
    if int(inputs) == 1:
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

    elif int(inputs) == 2:
        crit1 = input("Ingrese el criterio 1: ")
        minimo1 = float(input("Ingrese el mínimo 1: "))
        maximo1 = float(input("Ingrese el máximo 1: "))
        crit2 = input("Ingrese el criterio 2: ")
        minimo2 = float(input("Ingrese el mínimo 2: "))
        maximo2 = float(input("Ingrese el máximo 2: "))
        rta = controller.requerimiento1(catalog,crit1,minimo1,maximo1,crit2,minimo2,maximo2)
        print (f"Número de eventos dentro de ambos rangos: {rta[0]}")
        print (f"Número de artistas con reproducciones dentro de ambos rangos: {rta[1]}")

    elif int(inputs) == 3:
        minimo1 = float(input("Ingrese el mínimo 1 de Liveness: "))
        maximo1 = float(input("Ingrese el máximo 1 de Liveness: "))
        minimo2 = float(input("Ingrese el mínimo 2 de Speechiness: "))
        maximo2 = float(input("Ingrese el máximo 2 de Speechiness: "))
        rtaSongs = controller.requerimiento2(catalog,minimo1,maximo1,minimo2,maximo2)
        tamano = mp.size(rtaSongs)
        print (f"El total de pistas únicas es: {tamano}")
        shuffledKeys = mp.keySet(rtaSongs)
        for i in range(1,9):
            idSong = mp.get(rtaSongs,lt.getElement(shuffledKeys,i))
            print (f"Track {i}: {idSong['key']} with Valence {idSong['value'][0]} and Tempo {idSong['value'][1]}")

    elif int(inputs) == 4:
        minimo1 = float(input("Ingrese el mínimo de Valence: "))
        maximo1 = float(input("Ingrese el máximo de Valence: "))
        minimo2 = float(input("Ingrese el mínimo de Tempo: "))
        maximo2 = float(input("Ingrese el máximo de Tempo: "))
        rtaSongs = controller.requerimiento3(catalog,minimo1,maximo1,minimo2,maximo2)
        tamano = mp.size(rtaSongs)
        print (f"El total de pistas únicas es: {tamano}")
        shuffledKeys = mp.keySet(rtaSongs)
        for i in range(1,9):
            idSong = mp.get(rtaSongs,lt.getElement(shuffledKeys,i))
            print (f"Track {i}: {idSong['key']} with Valence {idSong['value'][0]} and Tempo {idSong['value'][1]}")

    elif int(inputs) == 5:
        generos = input("Ingrese la lista de géneros separados por comas (sin espacios): ")
        semaforo = int(input("Desea añadir un nuevo género a la búsqueda? (1- sí. 2- no) "))
        genSearch = generos.split(",")
        if semaforo == 1:
            genre = input("Nombre del nuevo género: ")
            tMin = float(input("Tempo mínimo: "))
            tMax = float(input("Tempo máximo: "))
            #mp.put(catalog['genres'],genre,0)
            mp.put(catalog['genArt'],genre,None)
            mp.put(catalog['range'],genre,[tMin,tMax])
            rang = mp.get(catalog['range'],genre)['value']
            mini,maxi = rang[0],rang[1]
            mp.get(catalog['genArt'],genre)['value'] = om.values(mp.get(catalog['info'],'tempo')['value'],mini,maxi)
            genSearch.append(genre)
        resultado = controller.requerimiento4(catalog,genSearch)
        counter = 0
        print("RESULTADOS REQUERIMIENTO 4: ")
        print (f"La cantidad total de reproducciones/eventos es: {resultado[0]}")
        for generooo in genSearch:
            counter += 1
            todosArt = mp.get(catalog['genArt'],generooo)['value']
            nArtistas = lt.getElement(resultado[2],counter)
            listaDiezArt = lt.getElement(resultado[3],counter)
            eachN = lt.getElement(resultado[1],counter)
            print (f'Resultados búsqueda {generooo}: ')
            print (f"La cantidad de reproducciones/eventos del género es: {eachN}")
            print (f"La cantidad de artistas únicos es: {nArtistas}")
            for numero in range(1,11):
                gente = lt.getElement(listaDiezArt,numero)
                print(f"Artista {numero}: {gente}")

    else:
        sys.exit(0)
sys.exit(0)
