# Ejercicios: Nivel 1
# 1. Crea una tupla vacía
tuple = tuple()

# 2. Cree una tupla que contenga los nombres de sus hermanas y sus hermanos ( los hermanos imaginarios están bien )
tuple_bro = ('Luciano')
tuple_sister = ('Eliana', 'Lila',)
# 3. Únete a las tuplas de hermanos y hermanas y asígnalo a los hermanos
brothers = tuple_bro + tuple_sister 

# 4. ¿Cuántos hermanos tienes?

len(brothers)

# 5. Modifique la tupla de los hermanos y agregue el nombre de su padre y su madre y asígnelo a family_members

# Agregamos el nombre del padre
brothers += ("José",)
# Agregamos el nombre de la madre
brothers += ("Marta",)
# Asigna la tupla modificada a family_members
family_members = brothers
print(family_members)


# Ejercicios: Nivel 2
# 1. Desempaquetar hermanos y padres de familiares
brothers = ("Juan", "Pedro", "María")
parents = ("José", "Marta")

hermano_uno, hermano_dos, hermano_tres = brothers
padre, madre = parents

print(hermano_uno, hermano_dos, hermano_tres)
print(padre, madre)

# 2. Crear tuplas de frutas, verduras y productos animales. Únase a las tres tuplas y asígnelo a una variable llamada food_stuff_tp.
frutas = ("manzana", "pera", "plátano")
verduras = ("lechuga", "tomate", "zanahoria")
productos_animales = ("carne", "pescado", "huevo")

# Combinar las tres tuplas
food_stuff_tp = frutas + verduras + productos_animales
print(food_stuff_tp)

# 3. Cambie la tupla about food_stuff_tp a una lista food_stuff_lt
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Corte el artículo del medio o los artículos de la tupla food_stuff_tp o la lista food_stuff_lt.
food_stuff_tp = food_stuff_tp[:len(food_stuff_tp) // 2] + food_stuff_tp[len(food_stuff_tp) // 2 + 1:]
print(food_stuff_tp)
# Cortar los elementos del medio de la lista
food_stuff_lt = food_stuff_lt[:len(food_stuff_lt) // 2] + food_stuff_lt[len(food_stuff_lt) // 2 + 1:]
print(food_stuff_lt)

# 5. Rebane los primeros tres artículos y los últimos tres artículos de la lista food_staff_lt
food_stuff_lt = food_stuff_lt[3:]
print(food_stuff_lt)
# Rebane los últimos tres artículos de la lista
food_stuff_lt = food_stuff_lt[:-3]
print(food_stuff_lt)

# 6. Eliminar la tupla food_staff_tp por completo
del food_stuff_tp
print(food_stuff_tp)

# 7. Verifique si existe un elemento en la tupla:
paises = ("Estonia", "Finlandia", "Islandia", "Noruega", "Suecia")
en_la_tupla = "Estonia" in paises
print(en_la_tupla)
en_la_tupla = "Islandia" in paises
print(en_la_tupla)

# - Comprueba si 'Estonia' es un país nórdico
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
en_la_lista = 'Estonia' in nordic_countries
print(en_la_lista)

# - Comprueba si 'Islandia' es un país nórdico
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Verifica si 'Islandia' está en la lista
en_la_lista = 'Islandia' in nordic_countries

print(en_la_lista)