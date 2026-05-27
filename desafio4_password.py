# Programa para control contraseña
contraseña_establecida = 'hola123' # establecemos la variable con la contraseña
intentos = 3 # Iniciamos el contador con 3 intentos

while intentos > 0: # Inciacimos el ciclo while con la condición
    contraseña_ingresada = input('Ingrese su contraseña:\n') # Solicitamos el ingreso de la contraseña
    if contraseña_ingresada == 'salir': # Hacemos la primera condición dentro del ciclo while
        break
    elif contraseña_ingresada != contraseña_establecida:  # Hacemos la segunda condición dentro del ciclo while
        intentos -=1
        print(f'Contraseña incorrecta, le quedan {intentos} intentos')
    elif contraseña_ingresada == contraseña_establecida: # Hacemos la tercera condición dentro del ciclo while
        print('Acceso concedido')
    break
 
if intentos == 0: # Hacemos una ultima condicional para cuando el numero de intentos es igual a cero fuera del ciclo while
    print(f'Acceso bloqueado')

    
