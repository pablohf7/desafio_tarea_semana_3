# Creamos el programa menu
# Creamos el ciclo while
opcion = ''
while opcion != 5:
    print('')
    print(
    'PROGRAMA DE CALCULO\n'
    '--------------------------------------------\n'
    'MENU:\n'
    'Opción 1 - Sumar dos numeros\n'
    'Opción 2 - Restar dos numeros\n'
    'Opción 3 - Comprar dos numeros\n'
    'Opción 4 - Mostrar los numeros del 1 al N\n'
    'Opción 5 - Salir')
    print('')
    opcion = int(input('Ingrese la opción:\n'))
    if opcion == 1:
        num1 = int(input('Ingrese el valor del numero 1:\n'))
        num2 = int(input('Ingrese el valor del numero 2:\n'))
        print('RESULTADO: La suma de los dos numeros es: ', num1+num2)
    elif opcion == 2:
        num1 = int(input('Ingrese el valor del numero 1:\n'))
        num2 = int(input('Ingrese el valor del numero 2:\n'))
        print('RESULTADO: La resta de los dos numeros es: ', num1-num2)
        print('')
    elif opcion == 3:
        num1 = int(input('Ingrese el valor del numero 1:\n'))
        num2 = int(input('Ingrese el valor del numero 2:\n'))
        print('RESULTADO\n')
        # Comparar los dos numeros
        if num1 == num2:
            print('Los numeros son iguales')
        else:
            print('Los numeros son diferentes')
    elif opcion == 4:
    # Mostrar los numeros del numero 1 al N
        print('')
        num = int(input('Ingrese un numero:\n'))
        lista = []
        for i in range(1,num+1,1):
            lista.append(i)
        print('RESULTAdO\n')
        print(f'La lista de numeros es:\n{lista}')


