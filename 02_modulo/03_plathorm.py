"""
Platform 

- Con platform podemos conocer configuraciones y caracteristicas del sistemas operativo actual que estamos  

"""

from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

#Conocer sistema operativo
print(platform())
print(platform(1))
print(platform(0,1))

# Conocer ejcutante de python
print(machine())

# Conocer procesador 
print(processor())

# Nombre del sistema operativo
print(system())

# Versión del sistema operativo
print(version())

# Versión de python 
print(python_implementation())

# Info de Python 
print(python_version_tuple())