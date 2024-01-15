# Editing and Deleting in Strings

s = 'hello world'
s[0] = 'H'

# Python strings are immutable

s = 'hello world'
del s
print(s)

s = 'hello world'
del s[-1:-5:2]
print(s)