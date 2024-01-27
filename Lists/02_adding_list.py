# Adding Items to a List


# append
L = [1,2,3,4,5]
L.append(True)
print(L)

# extend
L = [1,2,3,4,5]
L.extend([6,7,8])
print(L)

L = [1,2,3,4,5]
L.append([6,7,8])
print(L)

L = [1,2,3,4,5]
L.extend('delhi')
print(L)

# insert
L = [1,2,3,4,5]

L.insert(1,100)
print(L)

# Editing items in a List

L = [1,2,3,4,5]

# editing with indexing
L[-1] = 500

# editing with slicing
L[1:4] = [200,300,400]

print(L)