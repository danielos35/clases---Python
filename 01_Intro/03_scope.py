#El alcance de una variable dentro de una función NO sobrepasa la función en si, funciona igual que en JS
def alcance():
    nombre = 'Daniel'; 
    print(nombre);
    
    
#Las variables externas, son concideradas dentro de una función, desde que esta sean leidas previamente, en caso de no ser así se tendria dos variables diferenes, con el mismo nombre, una dentro de la función y otra fuera 
variable = 'VariableExterna';
def alcanceDos():
    variable = 'Hola Mundo'; 
    print(variable); 

alcanceDos()
print(variable)

#En caso de querer declarar una variable global dentro de la función, utilizamos esta misma palabra reservada  global
variableGlobal =  'Soy una variable global'; 
def conVariablesGlobales():
    global variableGlobal; 
    print(variableGlobal)
    variableGlobal = "Test Dos";
    
conVariablesGlobales()
print(variableGlobal)


#Recursividad, hablamos de recursividad cuando una función se invoca a si misma, esto puede ser riesgoso si no se tiene en consideración que se puede crear un blucle, estas también puede consumir mucha memoria y por tal ser tambien ineficientes