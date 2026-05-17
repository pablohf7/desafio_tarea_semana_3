# Programa creado para controlar acceso

#Creamos el bucle while para repetir la ejecución del programa
opcion = ''
while opcion != 'no':

    # Programa creado para controlar acceso
    nombre = input('Ingrese su nombre:\n') # Solicitamos el nombre
    edad = int(input('Ingrese su edad:\n')) # Solicitamos la edad
    tiene_entrada = input('¿Tiene entrada?(s/n):\n') # Preguntamos si tiene entrada
    lista_vip = input('¿Esta en la lista VIP?(s/n):\n') # Consultamos si esta en la lista VIP

    #Creamos los condicionales para control del acceso 
    if edad >= 18:
        print(f'{nombre}, eres mayor de edad') 
    elif tiene_entrada == 's' or lista_vip == 's':
        print(f'Puedes ingresar')
    else:
        print('No puedes ingresar')


  
