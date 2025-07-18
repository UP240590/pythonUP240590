# Define initial IT companies set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Find the length of the set it_companies
print("Length of it_companies:", len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("After adding Twitter:", it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Samsung', 'Intel', 'Netflix'])
print("After adding multiple companies:", it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Google')
print("After removing Google:", it_companies)

# 5. Difference between remove and discard:
#    - remove() raises an error if the item does not exist
#    - discard() does NOT raise an error if the item does not exist
