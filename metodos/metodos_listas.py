listas_animales = ['Perro','Gato','Delfin','Pantera']
lista_compras = ['cepillo','pasta de dientes','jabon']
lista_numeros = [5,48,1,98,2563,-23]

print(type(listas_animales))

# El método LEN (length, largo = tamaño) permite conocer la cantidad de elementos de una lista 
print(len(listas_animales))

# el metodo append agrega un nuevo elemento al final de la lista
print()
nuevo_animal = input('Agrege un nuevo animal a la lista: ')
listas_animales.append(nuevo_animal)
print(len(listas_animales))
print(listas_animales)

print()
# el metodo insert permite agregar un elemento en un lugar (indice) especifico
otro_animmal = input('Agregue un nuevo animal a la lista: ')
listas_animales.insert(2,otro_animmal)
print(len(listas_animales))
print(listas_animales)

print()
# el metodo extend permite agregar varios elementos a una lista
# agregamos una lista ya creada, uniendo ambas listas
listas_animales.extend(lista_compras)
print(len(listas_animales))
print(listas_animales)

# agregamos una lista creada manualmente
listas_animales.extend(['oso pardo','panda','oso polar'])
print(len(listas_animales))
print(listas_animales)

print()
# el metodo pop permite eliminar elementos de una lista
# si el metodo pop no se le entregan elementos, elimina el ultimo elemento de la lista
listas_animales.pop()
print(len(listas_animales))
print(listas_animales)

# si al metodo pop le indico el argumento indice, elimina el elemento especificado
listas_animales.pop(0)
print(len(listas_animales))
print(listas_animales)

# si al metodo pop le indico el argumento indice -1, elimina el ultimo elemento especificado de la lista
listas_animales.pop(-1)
print(len(listas_animales))
print(listas_animales)

print()
# el metodo remove elimina un elemento por su valor
listas_animales.remove('oso pardo')
print(len(listas_animales))
print(listas_animales)

print()
# el metodo clear elimina todos los elementos de la lista
listas_animales.clear()
print(len(listas_animales))
print(listas_animales)

print()
# el metodo sort ordena una lista de cadenas de texto alfabeticamente
lista_compras.sort()
print(len(lista_compras))
print(lista_compras)

# el metodo reverse ordena la lista al revez 
lista_compras.reverse()
print(lista_compras)

print()
# el metodo sort ordena una lista de numeros de manera ascendente
lista_numeros.sort()
print(len(lista_numeros))
print(lista_numeros)

# el metodo reverse ordena la lista de numeros de manera descendente
lista_numeros.reverse()
print(lista_numeros)