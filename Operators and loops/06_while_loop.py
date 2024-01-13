# While loop example -> program to print the table
# Program -> Sum of all digits of a given number
# Program -> keep accepting numbers from users till he/she enters a 0 and then find the avg

number = int(input('enter the number'))

i = 1

while i<11:
  print(number,'*',i,'=',number * i)
  i += 1

  # while loop with else 

x = 1

while x < 3:
  print(x)
  x += 1

else:
  print('limit crossed')