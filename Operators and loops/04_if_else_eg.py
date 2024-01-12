# if-else examples
# 1. Find the min of 3 given numbers
# 2. Menu Driven Program

# min of 3 number

a = int(input('first num'))
b = int(input('second num'))
c = int(input('third num'))

if a<b and a<c:
  print('smallest is',a)
elif b<c:
  print('smallest is',b)
else:
  print('smallest is',c)

# menu driven calculator
menu = input("""
Hi! how can I help you.
1. Enter 1 for pin change
2. Enter 2 for balance check
3. Enter 3 for withdrawl
4. Enter 4 for exit
""")
if menu == '1':
  print('pin change')
elif menu == '2':
  print('balance')
else:
  print('exit')