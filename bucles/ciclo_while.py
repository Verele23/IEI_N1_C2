# ciclo while es usado para ejecutar un set de tareas una cantidad determinada de veces
contador = 0
while contador < 10: 
    print(contador)
    contador = contador + 1


print('ciclo while mientras contador sea < 10')

contrasena = 'eureka'
intento = 0
while intento < 3: 
    contrasena_usuario = input('ingrese contraseña: ')
    if contrasena_usuario == contrasena:
        print('contraseña correcta!')
    else:
        intento += 1
        if intento < 3:
            print('contraseña incorrecta, intente nuevamente.')
        else:
            print('contraseña incorrecta, cerrando sistema!')
    
    

