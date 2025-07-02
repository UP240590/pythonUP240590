#Ejercicios nivel 1

First_Name='Rafael'             #Declarar variable primer nombre
Last_Name='Romo'                #Declarar variable apellido
Full_Name='Rafael Romo Franco'  #Declarar variable nombre
Country='México'                #Declarar variable pais
City='Aguascalientes'           #Declarar variable ciudad
Age='21'                        #Declarar variable edad
Year=2025                       #Declarar variable año
Is_mrried='no'                  #Declarar variable
Is_true='yes'                   #Declarar variable
Is_light=''                     #Declarar variable

print(type(Full_Name))
print(type(First_Name))
print(type(Last_Name))

#Ejercicios nivel 2
a=5
b=4
variable_total=a+b
variable_diff=a-b
variable_product=a*b
variable_division=a/b
variable_remainder=a%b
variable_exp=a**b
Floor_division=a//b

print("\n" + "=" * 40)
radius = 30                    #metros
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius


print(f"Para el circulo con radios {radius} metros:")
print(f"Area del circulo = {area_of_circle: .2f} metros cuadrados")
print(f"Circunferencia del circulo = {circum_of_circle: .2f} metros")
print()

user_radius = float(input("Introduce el radio del circulo en metros:" ))

user_area = 3.14 * user_radius ** 2

print(f"Para el circulo con radio {user_radius} metros: ")
print(f"Area = {user_area: .2f} metros cuadrados")

print("\n" + "=" * 40 )
print("Please provide the following information:")


First_Name = input("Enter your first name: ")
Last_Name = input("Enter your last name: ")
Country = input("Enter your country: ")
age = input("Enter your age: ")


print("\n" + "=" * 40 )
print("COLLECTED INFORMATION:")
print("=" * 40)
print(F"First Name: {First_Name}")
print(f"Last Name: {Last_Name}")
print(f"Country: {Country}")
print(f"Age: {Age}")


