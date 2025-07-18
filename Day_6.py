# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers
sisters = ('Anna', 'Bella')
brothers = ('John', 'Mike')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# 4. How many siblings do you have?
num_siblings = len(siblings)
print("Number of siblings:", num_siblings)

# 5. Modify the siblings tuple and add the name of your father and mother
family_members = siblings + ('Father', 'Mother')
print("Family members:", family_members)
