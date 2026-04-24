# operadores aritmeticos

numero_1 = 45
numero_2 = 12
numero_3 = 0
cadena_1 = 'GG'
cadena_2 = 'GGWP'

# operador suma +
suma = numero_1 + numero_2
print(suma)
print(type(suma))

# operador resta -
print()
resta = numero_1 - numero_2
print(resta)
print(type(resta))

#operador multiplicacion *
print()
multiplicacion = numero_1 * numero_2
print(multiplicacion)
print(type(multiplicacion))

# operador division /
print()
division = numero_1 / numero_2
print(division)
print(type(division))
# una division con denominador 0 no esta definida, no se puede hacer
# siempre hay que revisar que el denominador sea distinto de 0
#print(numero_1 / numero_3)

# operador suma y multiplicacion tambien se aplican sobre cadenas de textos
print(cadena_1 + cadena_2)
print(cadena_1 + str(numero_1))
print(cadena_1 * numero_2)

