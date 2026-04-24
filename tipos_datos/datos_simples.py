# Tipos de datos en Python

# con el simbolo # escribo comentarios que no se ejecutan con el codigo

variable_texto = 'buen dia queridos estudiantes'
variable_texto_multiple_lineas = '''
esto es un texto 
en multiples lineas
'''

varable_entero = 25
variable_decimal = 2.5
variable_booleana = True


# Tipo de dato STRING str
print(variable_texto)
# Tipo de dato INTEGER int
print(varable_entero)
# Tipo de dato FLOATING float
print(variable_decimal)
# Tipo de dato BOOLEAN bool
print(variable_booleana)

print(type(variable_texto))
print(type(varable_entero))
print(type(variable_decimal))
print(type(variable_booleana))

print(dir(variable_texto))
print(variable_texto.title())
print(variable_texto.upper())
print(variable_texto.lower())

print(dir(varable_entero))
print(varable_entero.is_integer())
print(variable_decimal.is_integer())

print(dir(variable_booleana))
print(dir(variable_decimal))
