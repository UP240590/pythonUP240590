# Define sets A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 28, 27}

# 1. Join A and B
union_AB = A.union(B)
print("Union of A and B:", union_AB)

# 2. Find A intersection B
intersection_AB = A.intersection(B)
print("Intersection of A and B:", intersection_AB)

# 3. Is A subset of B
print("Is A subset of B?", A.issubset(B))

# 4. Are A and B disjoint sets
print("Are A and B disjoint?", A.isdisjoint(B))

# 5. Join A with B and B with A
print("A union B:", A.union(B))
print("B union A:", B.union(A))  # Same result

# 6. Symmetric difference between A and B
symmetric_diff = A.symmetric_difference(B)
print("Symmetric difference:", symmetric_diff)

# 7. Delete the sets completely
del A
del B
# print(A)  # Uncommenting this would raise a NameError
