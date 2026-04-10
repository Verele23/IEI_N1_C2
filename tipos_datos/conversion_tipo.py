nombre_personal = input('ingrese su nombre: ')
saludo = 'buen dia '
print(type(nombre_personal))
print(nombre_personal)

# CONCATENACION de cadenas de texto
print(saludo + nombre_personal)

str_numero_entero = input('ingrese un numero entero: ')
numero_entero = int(str_numero_entero)
numero_decimal = float(str_numero_entero)
print(type(numero_entero))
print(type(numero_decimal))
print(numero_entero)
print(numero_decimal)

numero_uno = 25
numero_dos = 50

# La operacion + con 2 numeros, opera aritmeticamente sumandolos y entregando el resultado
print(numero_uno + numero_dos)
# La operacion + con 2 cadenas de texto, opera sematicamente colocandolos entregando sumandolos y entregando el string resultante
print(saludo + str_numero_entero)
# la operacion + con 2 tipos de datos distintos arroja ERROR
# print(str_numero_entero + numero_dos)

# un string no vacio siempre retorna true al convertirlo a booleano, porque tiene contenido.
# si el string estuviera vacio, en ese caso seria false.
# str_booleano = 'true'
int_booleano = 1

#print(type(str_booleano))
print(type(int_booleano))

#booleano = bool(str_booleano)
otro_booleano = bool(int_booleano)

#print(booleano)
#print(type(booleano))
print(type(otro_booleano))

