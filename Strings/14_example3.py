# Write a program which can remove a particular character from a string.
s = input('enter the string')
term = input('what would like to remove')

result = ''

for i in s:
  if i != term:
    result = result + i

print(result)



# Write a program that can check whether a given string is palindrome or not.


s = input('enter the string')
flag = True
for i in range(0,len(s)//2):
  if s[i] != s[len(s) - i -1]:
    flag = False
    print('Not a Palindrome')
    break

if flag:
  print('Palindrome')