# 1.Concatene la cadena 'Treinta', 'Días', 'De', 'Pitón' a una sola cadena, 'Treinta días de Python'.
a= 'Treinta'
b='Dias'
c='De'
d='Python'
print(f'1.{a} {b} {c} {d}\n')

# 2.Concatene la cadena 'Codificación', 'Para', 'Todos' a una sola cadena, 'Codificación para todos'.

code ='Codificación'
para = 'Para'
todos='Todos'

print(f'2.{code} {para} {todos}\n')

# 3.Declare una variable llamada empresa y asígnela a un valor inicial "Codificación para todos".

empresa = "Codificación para todos"

# 4.Imprima la compañía variable usando imprimir ( ).

print(f'4. {empresa}\n')

# 5.Imprima la longitud de la cadena de la empresa utilizando len ( ) método y imprimir ( ).
print(f'5. {len(empresa)} \n')

# 6.Cambia todos los caracteres a letras mayúsculas usando upper( ) método.

print(f'6. {empresa.upper()} \n')

# 7.Cambie todos los caracteres a letras minúsculas usando lower() método.

print(f'7. {empresa.lower()} \n')

# 8.Utilice los métodos de capitalize(), title(), swapcase() para formatear el valor de la cadena Codificación para todos.

print(f'8. {empresa.capitalize()} \n {empresa.title()}\n {empresa.swapcase()}\n')

# 9.Cortar (slice) la primera palabra de Codificación para todos cuerda.

print(f'9. {empresa[:12]}\n')

# 10.Marque si Codificación para todos string contiene una palabra Codificación usando el índice del método, find u otros métodos.
sub_string = 'Codificación'
print(f'10. {empresa.index(sub_string)}\n')
# 11.Reemplace la palabra codificación en la cadena 'Codificación para todos' en Python.

print(f'11. {empresa.replace("Codificación","Python")}\n')
# 12.Cambie Python para todos a Python para todos usando el método de reemplazo u otros métodos.
print(f'12. {empresa.replace("Python para todos","Todos para Python")}\n')
# 13.Divida la cadena 'Codificación para todos' usando el espacio como separador ( dividido ( ) ) .
print(f'13. {empresa.split(" ")}\n')
# 14."Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" dividió la cadena en la coma.
string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies = string.split(",")
print('14.',companies)
# 15.¿Cuál es el carácter en el índice 0 en la cadena Codificación para todos.
print(f'15. {empresa[0]}\n')
# 16.¿Cuál es el último índice de la cadena Codificación para todos.
print(f'16. {empresa[-1]}\n')
# 17.Qué carácter está en el índice 10 en la cadena "Codificación para todos.
print(f'17. {empresa[10]} \n')
# 18.Cree un acrónimo o una abreviatura para el nombre 'Python For Everyone'.
print(f'18. {empresa[0::18]} \n')
# 19.Cree un acrónimo o una abreviatura para el nombre 'Codificación para todos'.
print(f'19. {empresa[0::18]} \n')
# 20.Use el índice para determinar la posición de la primera aparición de C en Codificación para todos.
print(f'20. {empresa.find("C")} \n')
# 21.Use el índice para determinar la posición de la primera aparición de F en Codificación para todos.
print(f'21. {empresa.find("F")} \n')
# 22.Use rfind para determinar la posición de la última aparición de l en Codificación para todas las personas.
print(f'22. {empresa.rfind("l")} \n')
# 23.Use el índice o busque para encontrar la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puede terminar una oración con porque porque es una conjunción'
sentence = "No puede terminar una oración con porque porque es una conjunción"
index23 = sentence.find("porque")
print('23.', index23)

# 24.Use el índice para encontrar la posición de la última aparición de la palabra porque en la siguiente oración: "No puede terminar una oración porque porque porque es una conjunción'
index24 = sentence.rindex("porque")
print('\n24.', index24)
# 25.Corte la frase 'porque porque porque' en la siguiente oración: 'No puede terminar una oración con porque porque porque es una conjunción'

index25 = sentence[34:48]

print('\n25.', index25)
# 26.Encuentre la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puede terminar una oración con porque porque porque es una conjunción'
index26 = sentence.find("porque", 7)

print('\n26.', index26)
# 27.Corte la frase 'porque porque porque' en la siguiente oración: 'No puede terminar una oración con porque porque porque es una conjunción'
index27 = sentence.replace("porque porque porque", "")

print('\n27.', index27)
# 28.¿"Codificación para todos" comienza con una subcadena Codificación?
string = "Coding For All"
print(f'\n28. {string.startswith("Coding")}')

# 29.¿'Codificación para todos' termina con una subcadena codificación?
print(f'\n28. {string.endswith("coding")}')
# 30.'   Codificación para todos', elimine los espacios de arrastre izquierdo y derecho en la cadena dada.
text = '   Coding For All      '
trimmed_text = text.strip()
print('\n30.' ,trimmed_text)

'''31. ¿Cuál de las siguientes variables devuelve Verdadero cuando usamos el método isidentifier ():
30DaysOfPython
treinta_días_de_python 
'''
metodo_1='30DaysOfPython'
metodo_2='treinta_días_de_python'

print(f'\n31. {metodo_1.isidentifier()} {metodo_2.isidentifier()}')
'''32.La siguiente lista contiene los nombres de algunas de las bibliotecas de pitón:
 [ 'Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon' ]. Únete a la lista con un hash con una cadena espacial.'''

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = " # ".join(python_libraries)
print('\n32.' ,joined_libraries)

# 33.Use la nueva secuencia de escape de línea para separar las siguientes oraciones
sentences = ["I am enjoying this challenge.", "I just wonder what is next."]

joined_sentences = "\n".join(sentences)

print('\n33.' ,joined_sentences)
# 34.Use una secuencia de escape de pestaña para escribir las siguientes líneas.

data = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print('\n34.' ,data)

# 35.Use el método de formato de cadena para mostrar lo siguiente:

radius = 10
area = 3.14 * radius ** 2

print("\n35. The area of a circle with radius {} is {} meters square.".format(radius, area))
# 36. Haga lo siguiente utilizando métodos de formato de cadena:
print('\n36.')
print("8 + 6 = {}".format(8 + 6))
print("8 - 6 = {}".format(8 - 6))
print("8 * 6 = {}".format(8 * 6))
print("8 / 6 = {}".format(8 / 6))
print("8 % 6 = {}".format(8 % 6))
print("8 // 6 = {}".format(8 // 6))
print("8 ** 6 = {}".format(8 ** 6))