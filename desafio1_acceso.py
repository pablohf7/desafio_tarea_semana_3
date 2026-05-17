# Programa creado para controlar acceso
#Creamos el bucle while para repetir la ejecución del programa
opcion = ''
while opcion != 'no':

    # Imprimimos el nombre del programa
    print('PROGRAMA PARA CONTROL DE ACCESO')
    print('###############################')
    # Solitamos los datos para hacer el control de acceso
    nombre = input('Ingrese su nombre:\n') # Solicitamos el nombre
    edad = int(input('Ingrese su edad:\n')) # Solicitamos la edad
    tiene_entrada = input('¿Tiene entrada?(s/n):\n') # Preguntamos si tiene entrada
    lista_vip = input('¿Esta en la lista VIP?(s/n):\n') # Consultamos si esta en la lista VIP

    #Creamos los condicionales para control del acceso 
    if edad >= 18 and (tiene_entrada == 's' or lista_vip == 's') :
        print(f'{nombre}, puedes ingresar') 
    else:
        print(f'{nombre}, eres menor de edad y por lo tanto no puedes ingresar')
    print('-----------------------------------------------------------------------------------------------------')
    print('')
    # Preguntamos para validar a otra persona
    opcion = input('¿Desea validar otra persona?(si/no):\n')
   


  
