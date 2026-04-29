# ingreso de contraseña mediante siclo for

contrasena = 'eureka'
for numero in range(3):
    contrasena_usuario = input('ingrese contraseña: ')
    if contrasena_usuario == contrasena:
        print('contraseña correcta!')
        break
    else:
        if numero < 2:
            print('contraseña incorrecta, intente nuevamente.')
        else:
            print('contraseña incorrecta, cerrando sistema!')
