
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

#Valores por defecto 
    #En Python podemos configurar valores por defecto dentro de la declaración de la función
    
def miNombre(name="Daniel", lastName="Márquez"): 
    print(name, lastName)

miNombre()
miNombre("Sandra", "Alvarez")


#Return 
    #El retorno al igual que en JS, permite terminar la función en cierto punto en especifico de la misma
    
def retorno():
    nombre = 'Daniel retorno';
    return nombre

# En caso de pasar la función sin los parentesis no imprimirá la dirección en memoria
print(retorno)

#Así la veriamos de manera natural
print(retorno())


#None es una palabra reservada en Python, equivalente a null en JS
variableNone = None; 

