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

# Nivel 2: Asignación de calificación
score = int(input("Enter your score (0-100): "))

if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score <= 79:
    grade = 'B'
elif 60 <= score <= 69:
    grade = 'C'
elif 50 <= score <= 59:
    grade = 'D'
elif 0 <= score <= 49:
    grade = 'F'
else:
    grade = 'Invalid score'

print(f"Your grade is: {grade}")

# Determinar estación del año
month = input("Enter the month: ").capitalize()
autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]

if month in autumn:
    season = "Autumn"
elif month in winter:
    season = "Winter"
elif month in spring:
    season = "Spring"
elif month in summer:
    season = "Summer"
else:
    season = "Unknown"

print(f"The season is: {season}")

# Lista de frutas
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()

if new_fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit)
    print("Updated fruits list:", fruits)

# Nivel 3: Análisis de persona
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Verificar existencia de 'skills' y mostrar la habilidad del medio
skills = person.get('skills', [])
if skills:
    middle_skill = skills[len(skills) // 2]
    print("Middle skill:", middle_skill)
    print("Has Python skill:", 'Python' in skills)

    # Título profesional según habilidades
    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer.")
    elif {'Node', 'MongoDB', 'Python'}.issubset(skills):
        print("He is a backend developer.")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")
else:
    print("No skills found.")

# Estado civil y país
if person.get('is_married') and person.get('country') == 'Finland':
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name} lives in Finland. He is married.")