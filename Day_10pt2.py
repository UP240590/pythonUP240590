# Nivel 2

# Suma de 0 a 100
total = 0
for num in range(101):
    total += num
print(f"Suma total: {total}")

# Suma pares e impares
even_sum = 0
odd_sum = 0
for num in range(101):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print(f"Suma pares: {even_sum}")
print(f"Suma impares: {odd_sum}")