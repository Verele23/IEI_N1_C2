# colecciones de datos

# listas
# es una coleccion ordenada y mutable de datos de cualquier tipo

print('listas en python')
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