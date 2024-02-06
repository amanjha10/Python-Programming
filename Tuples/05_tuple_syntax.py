# tuple unpacking
a,b,c = (1,2,3)
print(a,b,c)

a,b = (1,2,3)
print(a,b)

a = 1
b = 2
a,b = b,a

print(a,b)

a,b,*others = (1,2,3,4)
print(a,b)
print(others)

# zipping tuples
a = (1,2,3,4)
b = (5,6,7,8)

tuple(zip(a,b))