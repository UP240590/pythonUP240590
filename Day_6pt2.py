# 1. Unpack siblings and parents from family_members
*all_siblings, father, mother = family_members
print("Siblings:", all_siblings)
print("Father:", father)
print("Mother:", mother)

# 2. Create fruits, vegetables and animal products tuples
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'spinach', 'broccoli')
animal_products = ('milk', 'cheese', 'egg')

# 3. Join the three tuples and assign it to food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products

# 4. Change the food_stuff_tp tuple to a list
food_stuff_lt = list(food_stuff_tp)

# 5. Slice out the middle item or items
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]
else:
    middle_items = [food_stuff_lt[middle_index]]
print("Middle item(s):", middle_items)

# 6. Slice out the first three and last three items
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# 7. Delete the food_stuff_tp tuple completely
del food_stuff_tp
# print(food_stuff_tp)  # This would raise an error if uncommented

# 8. Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)  # False
print('Iceland' in nordic_countries)  # True
