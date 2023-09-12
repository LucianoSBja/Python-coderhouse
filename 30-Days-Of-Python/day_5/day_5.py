# 1. Declara una lista vacia 
lista_vacia = []

# 2. Declare una lista con mas de 5 elementos.
list_element = ('eleme1', 'elemen2', 'elemen3', 4, 5)

# 3. Encuentra la longitud de tu lista
print(len(list_element))

# 4. Obtenga el primer elemento, el elemnto central y el ultimo de la lista
print(f'Primer elemento {list_element[0]}, elemento del medio {list_element[2]}  y el ultimo elemento {list_element[-1]} ')

# 5. Declare una lista llamada mixed_data_types, ponga su nombre (edad, altura, estado civil, dirección)
mixed_data_types = [28, 1.80, 'casado', 'Rivadavia 570']

# 6. Declare una variable de lista llamada it_companies y asigne valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Imprima la lista usando imprimir ()
print(it_companies)

# 8. Imprima el número de empresas en la lista
print(len(it_companies))

# 9. Imprima la primera, media y última empresa.
print(f'primera {it_companies[0]}, media {it_companies[3]} y ultima{it_companies[-1]}')

# 10. Imprima la lista después de modificar una de las empresas.
it_companies[0]='Instagram'
print(it_companies)

# 11. Agregue una empresa de TI a it_companies
it_companies.append('Facebook')
print(it_companies)

# 12. Inserte una compañía de TI en el medio de la lista de compañías
it_companies.insert(4,'MongoDB')
print(it_companies)

# 13. ¡Cambie uno de los nombres de it_companies a mayúscula ( IBM excluido! )
it_companies[0]= 'INSTAGRAM'
print(it_companies)

# 14. Únase a it_companies con una cadena '#; '
it_companies_unidas = '#;  '.join(it_companies)
print(it_companies_unidas)

# 15. Verifique si existe una determinada empresa en la lista it_companies.
print(f'Existe esta empresa? {"Apple" in it_companies}')

# 16. Ordene la lista usando el método sort ( )
it_companies.sort(reverse=True) 
print(f'Ordenar {it_companies}')

# 17. Invierta la lista en orden descendente utilizando el método inverso ( )
it_companies.reverse()
print(f'Ordenar  descendente {it_companies}')

# 18. Reduzca las primeras 3 empresas de la lista
del it_companies[0:3]
print(f'Eliminado los tres primeros {it_companies}')

# 19. Reduzca las últimas 3 compañías de la lista
del it_companies[-3:]
print(f'Eliminado los ultimos tres {it_companies}')

# 20. Eliminar la empresa o empresas de TI del medio de la lista 
it_companies.remove('IBM')
print(f'Eliminado el del medio {it_companies}')

# 21. Eliminar la primera compañía de TI de la lista
it_companies.remove('Google')
print(f'Eliminado el primero {it_companies}')

# 22. Reduzca la lista de las empresas o empresas de TI del medio
it_companies= ['Instagram', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Facebook']
it_companies_reducidas = it_companies[:5]
print(it_companies_reducidas)

# 23. Eliminar la última compañía de TI de la lista
it_companies_ultima = it_companies.pop(0)
print(it_companies_ultima)

# 24. Eliminar todas las empresas de TI de la lista
it_companies_todo = it_companies.clear()
print(it_companies_todo )

# 25. Destruye la lista de empresas de TI
del it_companies

# 26. Únase a las siguientes listas:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end + back_end

# 27. Después de unirse a las listas en la pregunta 26. Copie la lista unida y asígnela a una variable full_stack. Luego inserte Python y SQL después de Redux.

full_stack = (front_end + back_end).copy()
print(full_stack )


# Ejercicios: Nivel 2

# La siguiente es una lista de 10 estudiantes de edad: 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# - Ordena la lista 
ages.sort()

# - Encuentra la edad mínima y máxima
edad_minima = ages[0]
edad_maxima = ages[-1]

# - Agregue la edad mínima y la edad máxima nuevamente a la lista
ages.insert(0, edad_minima)
ages.append(edad_maxima)

# - Encuentre la edad media ( un elemento medio o dos elementos intermedios divididos por dos )
if len(ages) % 2 == 0:
  edad_media = (ages[len(ages) // 2] + ages[len(ages) // 2 - 1]) / 2
else:
  edad_media = ages[len(ages) // 2]

# - Encuentre la edad promedio ( suma de todos los artículos dividida por su número )
edad_promedio = sum(ages) / len(ages)

# - Encuentra el rango de las edades ( max menos min )
rango_edades = edad_maxima - edad_minima

# - Compare el valor de ( min - promedio ) y ( max - promedio ), uso abs ( ) método
diferencia_minima = abs(edad_minima - edad_promedio)
diferencia_maxima = abs(edad_maxima - edad_promedio)




# 1. Encuentra el país medio ( ies ) en el lista de países
paises = ["China", "Rusia", "EE. UU.", "Finlandia", "Suecia", "Noruega", "Dinamarca"]
pais_medio = paises[len(paises) // 2]

# 2. Divida la lista de países en dos listas iguales si es incluso un país más para la primera mitad.
if len(paises) % 2 == 0:
  primeros_tres_paises = paises[:3]
  otros_paises = paises[3:]
else:
  primeros_tres_paises = paises[:4]
  otros_paises = paises[4:]

# 3. [ 'China', 'Rusia', 'EE. UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca' ]. Desempaque los primeros tres países y el resto como países escandalosos.
primeros_tres_paises, otros_paises = paises[:3], paises[3:]