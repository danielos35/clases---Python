
#Forma de definir una función en Python

def imprimirNombre(nombre):
    print("mi nombre es "+ nombre);
    
imprimirNombre('Daniel')
imprimirNombre('Sandra')


#Python tiene funciones integradas por ejemplo print(), ver documentación en:https://docs.python.org/3/library/functions.html


#Se pueden pasar argumentos por su posición
def imprimirPorPosicion(a,b):
    print(a,b)
    
#Y también se pueden pasar paramtros por nombre
def imprimitPorNombre(primerNombre,segundoNombre):
    print("mi nombre es ", primerNombre," ",segundoNombre)
    
imprimitPorNombre(segundoNombre = "Márquez", primerNombre = "Daniel")

#Se pude combinar la forma en que se llaman las funciones, pero siempre se debe de indicar los argumentos posicionales y despues las palabras claves

def porPosicionYNombre(a,b,c):
    print("a= ",a,"b= ",b,"c= ",c);
    
porPosicionYNombre("HOLA C", b="testB", c="testC")