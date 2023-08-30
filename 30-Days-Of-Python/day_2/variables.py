# Day 2: 30 Days of python programming
import math
# Variables in Python

first_name = 'Luciano Ezequiel'
last_name = 'Soto Bonja'
full_name = 'Luciano Ezequiel Soto Bonja'
city= 'Argentina'
country='Chaco'
age= 28
year= 2023
is_married= True
skills=['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firsname':'Luciano',
    'lastname':'Soto',
    'country':'Chaco',
    'city':'Argentina'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Luciano', 'Soto', 'Chaco', 28, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)


# 1.Verificar tipo de datos
print('Tipo de dato de nombre ',type(first_name))
print('Tipo de dato de nombre ',type(person_info))
print('Tipo de dato de nombre ',type(skills))

# 2.Usando el len ( ) función incorporada, encuentre la longitud de su nombre
print('Longitud de su nombre: ', len(first_name))

# 3.Compare la longitud de su nombre y su apellido
print(f'Longitud de nombre: {len(first_name)} y Longitud de apellido: {len(last_name)}')
# 4.Declare 5 como num_one y 4 como num_two
num_one = 5
num_two = 4

total = num_one + num_two
print('Suma de numero', total)
resta = num_one - num_two
print('Resta de numero', resta)
multi = num_one * num_two
print('Resta de multiplica', multi)
divide = num_one / num_two
print('Resta de divide', divide)
resto = num_one % num_two
print('Resto de divicion', resto)
potencia =  num_one ** num_two
print('Potencia de numero', potencia)
floor_division= num_one // num_two
print('Fraccion ', floor_division)

# 5.El radio de un círculo es de 30 metros.

radio = 30
area_of_circle= math.pi * radio ** 2
print("Area de circulo", round(area_of_circle))
circun_of_circle = 2* math.pi * radio
print("Circunferencia", circun_of_circle)


radius = float(input("Ingrese el radio del círculo: "))
area_of_circle = math.pi * radius ** 2
print("El área del círculo es:", area_of_circle)
# 6.Use la función de entrada incorporada para obtener el nombre, apellido, país y edad de un usuario y almacene el valor en sus nombres de variables correspondientes

name = str(input('Diagem su nombre: '))
last = str(input('Diagem su apellido: '))
contry = str(input('Diagem su Pais: '))
age = int(input('Diagem su edad: ')
)
persona1 = f'{name} {last} {contry} {age}'
print(persona1)