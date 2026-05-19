# Programa creado para solicitar una palabra y luego haga varias acciones.

# Solicitamos el ingreso de la palabra
palabra_original = input('Ingrese una palabra: \n')
# cambiamos todas las letras de las palabras a minusculas
palabra = palabra_original.lower()

# repondemos a la pregunta de cuantos caracteres tiene la palabra ingresada
print(f'La palabra ingresada tiene {len(palabra)} caracteres')

# repodemos a la preguntas de cuantas vocales tiene
# creamos una lista de vocales
vocales = ['a','e','i','o','u']
# iniciamos el contador en cero
contador = 0

for letra in palabra:         # hacemos una ciclo for para recorrer la palabra
    for vocal in vocales:     # hacemos una un segundo ciclo for anidado para recorrer la lista de vocales
        if letra == vocal:    # hacemos el condicional para comparar la letra con las vocal para aumentar el contador
            contador += 1     # si la letra en la palabra es igual a una vocal en la lista vocales se suma un valor al contador
print(f'La cantidad de vocales en la palabra es: {contador}') # finalmente imprimimos la cantidad de vocales en la palabra 

# Repodemos a la preguntas de cuantas consonantes tiene
contador = 0
for letra in palabra:
     if (letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u' and letra !=' '):
             contador +=1    # hacemos el condicional para comparar la letra con las vocal para aumentar el contadorcontador += 1     # si la letra en la palabra es igual a una vocal en la lista vocales se suma un valor al contador
print(f'La cantidad de consonantes en la palabra es: {contador}') # finalmente imprimimos la cantidad de vocales en la palabra 

# Investigar si la palabra Python esta presente
# Para eso hacemos una condicioanal if y preguntamos si la palabra 'python' esta presente en la frase
if 'python' in palabra:
     print('La palabra python esta presente') # Si la palabra esta presente se imprime esto
else:
     print('La palabra python no esta presente') # Si la palabra no esta presente se imprime esto
          
