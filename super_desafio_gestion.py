# Programa para registro de estudiantes
estudiantes = {} # Hacemos un diccionario vacio para el registrar los estudiantes
# variable de control
opcion = ''

# Inciamos tres contadores en cero para contabilizar los estado de los estudiantes
aprobados = 0
reprobados = 0
observacion = 0

# hacemos un bucle while para registrar los estudinates
while opcion != 'no':
    print("\n=== REGISTRO DE ESTUDIANTE ===")
    # Ingresamos los datos de los estudiantes
    nombre = input('Ingrese nombre:\n')
    nota = int(input('Ingrese nota:\n'))
    asistencia = int(input('Ingrese sistencia(%):\n'))

    # Evaluar estado del estudiante
    if nota >= 7 and asistencia >= 75:
        estado = "Aprobado"
        aprobados +=1

    elif nota < 7:
        estado = "Reprobado"
        reprobados +=1

    else:
        estado = "Observación"
        observacion +=1

    # Guardamos los datos en el diccionario
    estudiantes[nombre] = {
            'nota': nota,
            'asistencia': asistencia,
            'estado': estado
        }
            
    # Preguntar si desea continuar
    opcion = input("\n¿Desea agregar otro estudiante? (si/no): ")

# Mostramos los resultados por cada estudiante
print("\n=== RESULTADOS ===")

for nombre, datos in estudiantes.items():
    print(f"{nombre}: {datos['estado']}")
  
# Mostramos el resumen final
print("\n=== RESUMEN FINAL ===")

print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")
print(f"Observación: {observacion}")


