# Difference between Lists and Tuples
    # Syntax
    # Mutability
    # Speed
    # Memory
    # Built in functionality
    # Error prone
    # Usability

import time 

L = list(range(100000000))
T = tuple(range(100000000))

start = time.time()
for i in L:
  i*5
print('List time',time.time()-start)

start = time.time()
for i in T:
  i*5
print('Tuple time',time.time()-start)

import sys

L = list(range(1000))
T = tuple(range(1000))

print('List size',sys.getsizeof(L))
print('Tuple size',sys.getsizeof(T))