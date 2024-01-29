# List Comprehension

# Add 1 to 10 numbers to a list
L = []

for i in range(1,11):
  L.append(i)

print(L)

L = [i for i in range(1,11)]
print(L)

# scalar multiplication on a vector
v = [2,3,4]
s = -3
# [-6,-9,-12]

[s*i for i in v]

# Add squares
L = [1,2,3,4,5]

[i**2 for i in L]

# Print all numbers divisible by 5 in the range of 1 to 50

[i for i in range(1,51) if i%5 == 0]

# find languages which start with letter p
languages = ['java','python','php','c','javascript']

[language for language in languages if language.startswith('p')]

# Nested if with List Comprehension
basket = ['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','grapes','banana']

# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'

[fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]

# Print a (3,3) matrix using list comprehension -> Nested List comprehension
[[i*j for i in range(1,4)] for j in range(1,4)]

# cartesian products -> List comprehension on 2 lists together
L1 = [1,2,3,4]
L2 = [5,6,7,8]

[i*j for i in L1 for j in L2]