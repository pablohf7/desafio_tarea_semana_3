# Creamos el programa menu
# Creamos el ciclo while con el menu
opcion = ''
while opcion != 5:
    print('')
    print(
    'PROGRAMA DE CALCULO - VERSIÓN 1.0\n'
    '--------------------------------------------\n'
    'MENU:\n'
    'Opción 1 - Sumar dos numeros\n' 
    'Opción 2 - Restar dos numeros\n'
    'Opción 3 - Comprar dos numeros\n'
    'Opción 4 - Mostrar los numeros del 1 al N\n'
    'Opción 5 - Salir')
    print('')
    opcion = int(input('Ingrese la opción:\n')) # Solitamos el ingreso de la opción
    if opcion == 1:  # Al seleccionar la opción 1, solicitamos el valor de los dos numeros para sumarlos
        num1 = int(input('Ingrese el valor del numero 1:\n'))
        num2 = int(input('Ingrese el valor del numero 2:\n'))
        print('RESULTADO: La suma de los dos numeros es: ', num1+num2) # Imprimimos la suma de los dos numeros
    elif opcion == 2: # Al seleccionar la opción 2, solicitamos el valor de los dos numeros para restarlos
        num1 = int(input('Ingrese el valor del numero 1:\n'))
        num2 = int(input('Ingrese el valor del numero 2:\n'))
        print('RESULTADO: La resta de los dos numeros es: ', num1-num2) # Imprimimos la resta de los dos numeros
        print('')
    elif opcion == 3: # Al seleccionar la opción 3, solicitamos el valor de los dos numeros para compararlos
        num1 = int(input('Ingrese el valor del numero 1:\n'))
        num2 = int(input('Ingrese el valor del numero 2:\n'))
        print('RESULTADO\n')
        # Hacemos tres condicionales if para comparar los dos numeros y dependiedo de la condición se imprime el resultado
        if num1 == num2:
            print('Los numeros son iguales')
        if num1 > num2:
            print(f'El numero {num1} es mayor que el numero {num2}')
        if num1 < num2:
            print(f'El numero {num2} es mayor que el numero {num1}')
    elif opcion == 4: # Al seleccionar la opción 3, solicitamos el valor de un numero, para imprimer del 1 hasta ese numero
    # Mostrar los numeros del numero 1 al N
        print('')
        num = int(input('Ingrese un numero:\n')) # Solicitamos el valor del numero
        lista = [] # Creamos una lista vacia
        for i in range(1,num+1,1): # Creamos un ciclo for para llenar la lista de acuedo al numero ingresado
            lista.append(i)
        print('RESULTAdO\n')
        print(f'La lista de numeros es:\n{lista}') # Imprimimos la lista del 1 hasta el numero ingresado
    elif opcion != 1 or 2 or 3 or 4 or 5:
        print('INGRESE UNA OPCIÓN VALIDA POR FAVOR') # Si no se ingresa una de la opciones del menu se imprime este mensaje



