cadena = "acitametaM ,5.8 ,otipeP ordeP"

# Paso 1: Dar vuelta la cadena
cadena_volteada = cadena[::-1]

# Paso 2: Extraer nombre y apellido
nombre_alumno = cadena_volteada.split(',')[0].strip()

# Paso 3: Extraer la nota
nota =  cadena_volteada.split(',')[1].strip()

# Paso 4: Extraer la materia
materia = cadena_volteada.split(',')[2].strip()

# Paso 5: Formatear la cadena para mostrar
cadena_formateada = f"{nombre_alumno} ha sacado un {nota} en {materia}"

# Mostrar por pantalla la cadena formateada
print(cadena_formateada)
