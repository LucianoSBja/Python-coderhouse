def calcular_nota_final(nota1, nota2, nota3):
    porcentaje_nota1 = 0.20
    porcentaje_nota2 = 0.30
    porcentaje_nota3 = 0.50
    
    nota_final = (nota1 * porcentaje_nota1) + (nota2 * porcentaje_nota2) + (nota3 * porcentaje_nota3)
    return nota_final

# Obtener las notas del usuario
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))

# Calcular la nota final
nota_final = calcular_nota_final(nota1, nota2, nota3)

# Mostrar la nota final
print(f"La nota final del estudiante es: {nota_final}")
