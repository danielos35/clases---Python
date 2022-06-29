
#Diccionario, estructura de datos iterable y mutable, son los objetos en JS
diccionario = {'nombre':'daniel','apellido':'Marquez'}; 
# print(diccionario['nombre'])
# print(diccionario['apellido'])


#Iterar un diccionario y con el metodo sorted lo podemos ordenar
for key in sorted(diccionario.keys()):
    print(key)
    
for valores in diccionario.values():
    print(valores)
    
for items in diccionario.items():
    print(items)
    
    
#Agregar valores a un diccionario 
diccionario['segundoNombre']  = "felipe"; 
print(diccionario)
    
#Mutar valores
diccionario['nombre'] = 'Daniel-'
print(diccionario)

#agregar valores con update
diccionario.update( {'segundo apellido' : 'Alvarez'} ); 
print(diccionario   )

#Eliminar valores 
del diccionario['segundoNombre']; 
print(diccionario)

#Eliminar Ultimo elemento
diccionario.popitem(); 
print(diccionario)