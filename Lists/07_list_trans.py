# 2 ways to traverse a list
# itemwise
# indexwise

# itemwise
L = [1,2,3,4]

for i in L:
  print(i)

# indexwise
L = [1,2,3,4]

for i in range(0,len(L)):
  print(L[i])

# Zip
# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together.

# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
  
# Write a program to add items of 2 lists indexwise

L1 = [1,2,3,4]
L2 = [-1,-2,-3,-4]

list(zip(L1,L2)) 

[i+j for i,j in zip(L1,L2)]

L = [1,2,print,type,input]

print(L)