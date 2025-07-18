# Nivel 1: Edad para conducir
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# Comparación de edades
my_age = 25
your_age = int(input("Enter your age: "))

diff = abs(my_age - your_age)
if your_age > my_age:
    print(f"You are {diff} year{'s' if diff > 1 else ''} older than me.")
elif your_age < my_age:
    print(f"I am {diff} year{'s' if diff > 1 else ''} older than you.")
else:
    print("We are the same age.")

# Comparación de dos números
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")
