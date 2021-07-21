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
from DISClib.ADT import list as lt
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog, dataFile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    file = cf.data_dir + dataFile
    input_file = csv.DictReader(open(file, encoding="utf-8"),
                                delimiter=",")
    for event in input_file:
        model.addEvent(catalog,event)
    return catalog
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def requerimiento1(catalog,crit1,minimo1,maximo1,crit2,minimo2,maximo2):
    return model.requerimiento1(catalog,crit1,minimo1,maximo1,crit2,minimo2,maximo2)

def requerimiento3(catalog,minimo1,maximo1,minimo2,maximo2):
    return model.requerimiento3(catalog,minimo1,maximo1,minimo2,maximo2)