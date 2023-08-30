
'''
1.Declara tu edad como variable entera 
2.Declara tu altura como una variable flotante 
3.Declara una variable que almacena un número complejo
''' 

age= 28
height= 1.80
complex= 1 + 1j

''' 4. Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo y calcule un área de este área triangular ( = 0.5 x b x h ).'''

base=float(input('Ingresa la base: '))
height=float(input('Ingrese la altura: '))
area = 0.5 * base * height
print(f'El area del triangulo es: {area}')


'''Escriba un script que solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo. Calcule el perímetro del triángulo ( perímetro = a + b + c ).''' 

side_a =int(input('Ingrese lado a: '))
side_b =int(input('Ingrese lado b: '))
side_c =int(input('Ingrese lado c: '))

perimetro= side_a + side_b + side_c
print(f'El perimetro del triangulo es: {perimetro}')


''' 6.Obtenga longitud y ancho de un rectángulo con pront. Calcule su área ( área = longitud x ancho ) y perímetro ( perímetro = 2 x ( longitud + ancho ))'''

print("Ingrese la longitud del rectángulo:")
length = float(input())

print("Ingrese el ancho del rectángulo:")
width = float(input())

area = length * width
print("El Area es: ", area)

perimetro= 2*(length + width)
print("El Perimetro es: ", perimetro)


''' 7.Obtenga el radio de un círculo usando la solicitud. Calcule el área ( área = pi x r x r ) y circunferencia ( c = 2 x pi x r ) donde pi = 3.14.'''

print("Ingrese el radio de un circulo: ")
radio = float(input())

area = 3.14 * radio ** 2
print("El radio es: ", area)

circunferencia= 2 * 3.14 * radio
print("La circunferencia es: ", area)


'''Pendiente (m) y coeficiente lineal (b)'''
# Pendiente (m) y coeficiente lineal (b)
m = 2
b = -2

# Calcular la intersección en x (x-intercept)
x_intercept = -b / m

# Imprimir resultados
print(f"Pendiente (m): {m}")
print(f"Intersección en x: {x_intercept}")
print(f"Intersección en y: ({0}, {b})")


'''9.La pendiente es ( m = y2-y1 / x2-x1 ). Encuentra la pendiente y Distancia euclidiana entre el punto ( 2, 2 ) y el punto ( 6,10 )''' 

from math import sqrt

# Coordenadas de los puntos
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calcular la pendiente
slope = (y2 - y1) / (x2 - x1)

# Calcular la distancia euclidiana
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Imprimir resultados
print(f"Pendiente: {slope}")
print(f"Distancia euclidiana: {distance}")


''' 10.Compare las pendientes en las tareas 8 y 9.'''
#Pendiente de la tarea 1 y tarea 2
pendiente_tarea1 = 9
pendiente_tarea2 = 8
#Comparar las pendientes
if pendiente_tarea1 == pendiente_tarea2:
    print("Las pendientes son iguales.")
else:
    print("Las pendientes son diferentes.")


''' 11.Calcule el valor de y ( y = x ^ 2 + 6x + 9 ). Intente usar diferentes valores de x y descubra cuál será el valor de x y será 0.'''
def calculate_y(x):
    return x**2 + 6*x + 9

x_value_for_zero = -3
y_value_for_zero = calculate_y(x_value_for_zero)

print(f"Value of y for x = {x_value_for_zero}: {y_value_for_zero}")


'''12.Encuentre la longitud de 'python' y 'dragon' y haga una declaración de comparación de falsedad.''' 
length_python = len('python')
length_dragon = len('dragon')

falsy_comparison = length_python == length_dragon

print(f"Falsy Comparison: {falsy_comparison}")


'''13.Usar y operador para verificar si se encuentra 'encendido' tanto en 'python' como en 'dragon' '''
found_in_python = 'on' in 'python'
found_in_dragon = 'on' in 'dragon'

result_and = found_in_python and found_in_dragon

print(f"Result of AND operation: {result_and}")



'''14.Espero que este curso no esté lleno de jerga. Usar en operador para verificar si jerga está en la oración.''' 
sentence = "I hope this course is not full of jargon."
jargon_present = "jargon" in sentence

print(f"'jargon' is present in the sentence: {jargon_present}")


'''16.Encuentra la longitud del texto pitón y convertir el valor a flotar y convertirlo en cadena''' 
length_python = len('python')
float_length = float(length_python)
string_float_length = str(float_length)

print(f"Length as string float: {string_float_length}")

'''17.Los números pares son divisibles por 2 y el resto es cero. ¿Cómo verifica si un número está parejo o no está usando python?''' 
def is_even(number):
    return number % 2 == 0

number_to_check = int(input("Enter a number: "))
if is_even(number_to_check):
    print(f"{number_to_check} is even.")
else:
    print(f"{number_to_check} is odd.")


'''18.Compruebe si la división del piso de 7 por 3 es igual al valor invertido de 2.7.'''
result = 7 // 3 == int(2.7)
print(f"Result: {result}")

'''19.Compruebe si el tipo de '10' es igual al tipo de 10''' 
type_check = type('10') == type(10)
print(f"Type Check: {type_check}")

'''20.Compruebe si int ( '9.8' ) es igual a 10''' 
try:
    converted_value = int('9.8')
    print(f"Converted Value: {converted_value}")
except ValueError:
    print("Cannot convert '9.8' to an integer.")

'''21.Escriba un script que solicite al usuario que ingrese horas y tarifas por hora. Calcular el pago de la persona?

Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
''' 
hours_worked = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))

pay = hours_worked * rate_per_hour
print(f"Pay: {pay}")

'''Escriba un script que solicite al usuario que ingrese varios años. Calcule la cantidad de segundos que una persona puede vivir. Supongamos que una persona puede vivir cien años

Enter number of years you have lived: 100
You have lived for 3153600000 seconds.

'''
years = int(input("Enter the number of years: "))
seconds_in_a_year = 365 * 24 * 60 * 60
maximum_years = 100

if years > 0:
    if years <= maximum_years:
        total_seconds = years * seconds_in_a_year
        print(f"A person can live {total_seconds:,} seconds in {years} years.")
    else:
        print(f"Please enter a value less than or equal to {maximum_years}.")
else:
    print("Please enter a valid number of years greater than 0.")

'''Escriba un script de Python que muestre la siguiente tabla

1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''

print("Number   |   Squared   |   Cubed")
print("-------- | ----------- | -------")

for number in range(1, 11):
    squared = number ** 2
    cubed = number ** 3
    print(f"{number:<9} | {squared:<11} | {cubed}")
