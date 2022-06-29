"""
Modulos


- Los modulos en Python nos permiten hacer la aplicación mucho mas facil de mantener pues cada funcionalidad suele estar separada
- Los usaurios puede CREAR los modulos, o tambien CONSUMIR los modulos 

"""

# Importar un modulo -  palabra reservada import, nombre del modulo: 
# Los modulos pueden ser importados en una sola linea de texto, simplemente separandolos con coma
import imp
import math, sys

# Con dir podemos ver todas las entidades de un moduloS
print(dir(math))

# Importar entidades en especifico
from math import pi

# dar otro nombre a un modulo 
import os as sistemaOperativo

# Dar otro nombre a una entidad
from math import pi as numeroPI


# MODULO DES PYTHON: https://docs.python.org/3/py-modindex.html