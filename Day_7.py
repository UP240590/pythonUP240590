# Nivel 1

# 1. Conjunto de compañías de TI
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Longitud del conjunto
print("Longitud de it_companies:", len(it_companies))

# Añadir 'Twitter'
it_companies.add('Twitter')

# Insertar varias empresas
it_companies.update(['Intel', 'Cisco', 'Adobe'])
print("Conjunto actualizado:", it_companies)

# Eliminar una empresa
it_companies.remove('Google')  # Usar discard si no estás seguro que existe

# Diferencia entre remove y discard
# remove() lanza error si el elemento no existe
# discard() no lanza error si el elemento no existe

# -----------------------------
# Nivel 2
# -----------------------------

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28}

# Unión
print("Unión A ∪ B:", A.union(B))

# Intersección
print("Intersección A ∩ B:", A.intersection(B))

# A es subconjunto de B
print("¿A es subconjunto de B?", A.issubset(B))

# A y B son disjuntos
print("¿A y B son disjuntos?", A.isdisjoint(B))

# Unir B con A
print("Unión B ∪ A:", B.union(A))

# Diferencia simétrica
print("Diferencia simétrica A △ B:", A.symmetric_difference(B))

# Eliminar los conjuntos
del A
del B

# -----------------------------
# Nivel 3
# -----------------------------

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages)
print("Tamaño de la lista:", len(ages))
print("Tamaño del conjunto:", len(ages_set))
if len(ages) > len(ages_set):
    print("La lista es más grande porque tiene duplicados.")
else:
    print("El conjunto es igual o más grande.")

# Diferencias entre tipos de datos
print("\n📘 Tipos de datos en Python:")
print("Cadena: Una secuencia de caracteres, por ejemplo: 'Hola mundo'")
print("Lista: Colección ordenada y modificable, por ejemplo: [1, 2, 3]")
print("Tupla: Colección ordenada e inmutable, por ejemplo: (1, 2, 3)")
print("Conjunto: Colección no ordenada de elementos únicos, por ejemplo: {1, 2, 3}")

# Palabras únicas en una oración
sentence = "Soy profesor y me encanta inspirar y enseñar"
words = sentence.split()
unique_words = set(words)
print("\nPalabras únicas en la oración:", unique_words)
print("Número de palabras únicas:", len(unique_words))