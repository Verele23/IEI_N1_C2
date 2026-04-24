# colecciones de datos

# listas
# es una coleccion ordenada y mutable de datos de cualquier tipo

print('\nlistas')
mi_primera_lista =['Rodrigo Varela',25,True]

nombre_personal = input('ingrese su nombre: ')
print(type(mi_primera_lista)) 
print(mi_primera_lista)
print(mi_primera_lista[0])
print(mi_primera_lista[1])
mi_primera_lista[0] = nombre_personal
print(mi_primera_lista)
print(dir(mi_primera_lista))
mi_primera_lista.append(30)
print(mi_primera_lista)
mi_primera_lista.remove(30)
print(mi_primera_lista)

# diccionario dictionary => dict
# es una coleccion ordenada y mutable de pares de datos de cualquier tipo
# los datos de un diccionario ocupan el doble de espacio en la memoria
# deben almacenar la clave y el valor de cada dato

print('\ndiccionario')
mi_primer_diccionario = {'nombre': 'Rodrigo Varela','edad':25,'asistio a clases hoy?':True}
print(type(mi_primer_diccionario))
print(mi_primer_diccionario)

print(f'el primer elemento de mi diccionario es:{mi_primer_diccionario["nombre"]}')
mi_primer_diccionario['nombre'] = nombre_personal
print(mi_primer_diccionario)
mi_primer_diccionario['esta feliz']= True
print(mi_primer_diccionario)
print(dir(mi_primer_diccionario))
# mi primer diccionario modificado = mi primer_diccionario.clear()
# print(mi_primer_diccionario_modificado)

# conjuntos set 
# es una coleccion desordenada e inmutable de datos de cualquier tipo

print('\nconjuntos')
mi_primer_conjunto = {'dato 1', 45, False}
print(type(mi_primer_conjunto))
print(mi_primer_conjunto)
mi_primer_conjunto.add(25)
print(mi_primer_conjunto)

# tuplas tuple
# es una coleccion ordenada e inmutable de datos de cualquier tipo

print('\ntuplas')
mi_primera_tupla =('Rodrigo Varela',35,True)
print(type(mi_primera_tupla))
print(mi_primera_tupla[0])

# la tupla no permite asignar un nuevo valor para los elementos, la siguiente asignacion es invalida
# mi_primera_tupla[0] = nombre_personal

