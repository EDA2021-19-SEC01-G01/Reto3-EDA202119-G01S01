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
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """ Inicializa el catálogo

    Retorna el catálogo inicializado.
    """
    catalog = {'events': None,
                'info': None}

    catalog['events'] = lt.newList('ARRAY_LIST')
    catalog['info'] = mp.newMap(11,maptype='PROBING',loadfactor=0.5)
    catalog['artistas'] = mp.newMap(maptype='PROBING',loadfactor=0.5)
    catalog['songs']= mp.newMap(maptype="PROBING",loadfactor=0.5)
    mp.put(catalog['info'],'instrumentalness', om.newMap(omaptype='RBT',comparefunction=compare))
    mp.put(catalog['info'],'liveness', om.newMap(omaptype='RBT',comparefunction=compare))
    mp.put(catalog['info'],'speechiness', om.newMap(omaptype='RBT',comparefunction=compare))
    mp.put(catalog['info'],'danceability', om.newMap(omaptype='RBT',comparefunction=compare))
    mp.put(catalog['info'],'valence', om.newMap(omaptype='RBT',comparefunction=compare))
    mp.put(catalog['info'],'loudness', om.newMap(omaptype='RBT',comparefunction=compare))
    mp.put(catalog['info'],'tempo', om.newMap(omaptype='RBT',comparefunction=compare))
    mp.put(catalog['info'],'acousticness', om.newMap(omaptype='RBT',comparefunction=compare))
    mp.put(catalog['info'],'energy', om.newMap(omaptype='RBT',comparefunction=compare))
    mp.put(catalog['info'],'mode', om.newMap(omaptype='RBT',comparefunction=compare))
    mp.put(catalog['info'],'key', om.newMap(omaptype='RBT',comparefunction=compare))
    
    return catalog

# Funciones para agregar informacion al catalogo
def addEvent(catalog,event):
    lt.addLast(catalog['events'],event)
    criterios = mp.keySet(catalog['info'])
    for index in range(1,lt.size(criterios)+1):
        ordered = lt.getElement(criterios,index)
        mapa = mp.get(catalog['info'],ordered)['value']
        llave = float(event[ordered])
        if om.contains(mapa,llave):
            lt.addLast(om.get(mapa,llave)['value'],event)
        else:
            listaPerValue = lt.newList('ARRAY_LIST')
            lt.addLast(listaPerValue,event)
            om.put(mapa,llave,listaPerValue)
    autor,song = event["artist_id"], event["track_id"]
    if mp.contains(catalog["artistas"],autor):
        lt.addLast(mp.get(catalog["artistas"],autor)["value"],event)
    else:
        listaCero = lt.newList("ARRAY_LIST")
        lt.addLast(listaCero,event)
        mp.put(catalog["artistas"],autor,listaCero)

    if mp.contains(catalog["songs"],song):
        lt.addLast(mp.get(catalog["songs"],song)["value"],event)
    else:
        listaCero = lt.newList("ARRAY_LIST")
        lt.addLast(listaCero,event)
        mp.put(catalog["songs"],song,listaCero)


# Funciones para creacion de datos

# Funciones de consulta
def requerimiento1(catalog,crit1,minimo1,maximo1,crit2,minimo2,maximo2):
    group1 = om.values(mp.get(catalog['info'],crit1)['value'],minimo1,maximo1)
    return interseccion(group1, crit2, minimo2, maximo2)
    
def interseccion(lista1,crit2,minimo2,maximo2):
    """
    Encuentra los eventos que cumplen con ambas condiciones
    Retorna:
    tamaño, número de artistas
    
    """
    artists = lt.newList("ARRAY_LIST")
    nEvents = 0
    for repro in range(1,lt.size(lista1)+1):
        recorriendo1 = lt.getElement(lista1,repro)
        for each in range(1,lt.size(recorriendo1)+1):
            recorriendo = lt.getElement(recorriendo1,each)
            if float(recorriendo[crit2]) > minimo2 and float(recorriendo[crit2]) < maximo2:
                nEvents += 1
                artist = recorriendo["artist_id"]
                if lt.isPresent(artists, artist) == 0:
                    lt.addLast(artists,artist)

    return (nEvents, lt.size(artists))


# Funciones utilizadas para comparar elementos dentro de una lista
def compare(cosa1, cosa2):
    """
    Compara dos cosas
    """
    if (cosa1 == cosa2):
        return 0
    elif (cosa1 > cosa2):
        return 1
    else:
        return -1
# Funciones de ordenamiento
