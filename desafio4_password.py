# Programa para control contraseña
contraseña_establecida = 'hola123'
intentos = 3

while intentos > 0:
    contraseña_ingresada = input('Ingrese su contraseña:\n')
    if contraseña_ingresada == 'salir':
        break
    elif contraseña_ingresada != contraseña_establecida:
        intentos -=1
        print(f'Contraseña incorrecta, le quedan {intentos} intentos')
    elif contraseña_ingresada == contraseña_establecida:
        print('Acceso concedido')
    break
 
if intentos == 0:
        print(f'Acceso bloqueado')

    
