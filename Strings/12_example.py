# Example Programs

# Find the length of a given string without using the len() function

s = input('enter the string')

counter = 0

for i in s:
  counter += 1

print('length of string is',counter)

# Extract username from a given email. 
# Eg if the email is amanjha3232@gmail.com 
# then the username should be amanjha3232

s = input('enter the email')

pos = s.index('@')
print(s[0:pos])