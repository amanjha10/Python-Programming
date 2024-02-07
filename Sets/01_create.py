# A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).

# However, a set itself is mutable. We can add or remove items from it.

# Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

# Characterstics:

    # Unordered
    # Mutable
    # No Duplicates
    # Can't contain mutable data types

# empty
s = set()
print(s)
print(type(s))
# 1D and 2D
s1 = {1,2,3}
print(s1)
#s2 = {1,2,3,{4,5}}
#print(s2)
# homo and hetro
s3 = {1,'hello',4.5,(1,2,3)}
print(s3)
# using type conversion

s4 = set([1,2,3])
print(s4)
# duplicates not allowed
s5 = {1,1,2,2,3,3}
print(s5)
# set can't have mutable items
s6 = {1,2,[3,4]}
print(s6)

s1 = {1,2,3}
s2 = {3,2,1}

print(s1 == s2)