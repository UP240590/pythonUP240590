# Crear un diccionario vacío llamado perro
perro = {}

# Añadir información al diccionario perro
perro['nombre'] = 'Max'
perro['color'] = 'Marrón'
perro['raza'] = 'Labrador'
perro['patas'] = 4
perro['edad'] = 5

print("Diccionario de perro:", perro)

# Crear un diccionario del estudiante
estudiante = {
    'nombre': 'Rafael',
    'apellido': 'Romo',
    'género': 'Masculino',
    'edad': 20,
    'estado_civil': 'Soltero',
    'habilidades': ['Python', 'Comunicación'],
    'país': 'México',
    'ciudad': 'Guadalajara',
    'dirección': 'Calle Falsa 123'
}

# Obtener la longitud del diccionario del estudiante
print("\nLongitud del diccionario estudiante:", len(estudiante))

# Obtener el valor de 'habilidades' y verificar el tipo de dato
print("\nHabilidades:", estudiante['habilidades'])
print("Tipo de dato de habilidades:", type(estudiante['habilidades']))

# Modificar habilidades agregando una o dos habilidades
estudiante['habilidades'].append('HTML')
estudiante['habilidades'].append('Trabajo en equipo')

print("Habilidades actualizadas:", estudiante['habilidades'])

# Obtener las claves del diccionario como lista
keys = list(estudiante.keys())
print("\nClaves del diccionario:", keys)

# Obtener los valores del diccionario como lista
values = list(estudiante.values())
print("Valores del diccionario:", values)

# Convertir el diccionario a lista de tuplas usando items()
items = list(estudiante.items())
print("\nDiccionario como lista de tuplas:", items)

# Eliminar un elemento del diccionario
del estudiante['estado_civil']
print("\nDespués de eliminar 'estado_civil':", estudiante)

# Eliminar el diccionario completo
del estudiante