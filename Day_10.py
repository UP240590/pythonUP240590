# Nivel 1

# For de 0 a 10
for i in range(11):
    print(i, end=' ')
print()

# While de 0 a 10
i = 0
while i <= 10:
    print(i, end=' ')
    i += 1
print()

# For de 10 a 0
for i in range(10, -1, -1):
    print(i, end=' ')
print()

# While de 10 a 0
i = 10
while i >= 0:
    print(i, end=' ')
    i -= 1
print()

# Triángulo con #
for i in range(1, 8):
    print('#' * i)

print()

# Cuadrícula 8x8 de #
for _ in range(8):
    print('# ' * 8)

print()

# Cuadrados del 0 al 10
for i in range(11):
    print(f"{i} x {i} = {i*i}")

print()

# Lista de tecnologías
techs = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in techs:
    print(tech)

print()

# Números pares 0-100
for num in range(0, 101, 2):
    print(num, end=' ')
print()

# Números impares 0-100
for num in range(1, 101, 2):
    print(num, end=' ')
print()

