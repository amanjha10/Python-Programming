# login program and indentation
# email -> python_programming@gmail.com
# password -> 1234

email = input('enter email')
password = input('enter password')

if email == 'python_programming@gmail.com' and password == '1234':
  print('Welcome')
elif email == 'python_programming@gmail.com' and password != '1234':
  # tell the user
  print('Incorrect password')
  password = input('enter password again')
  if password == '1234':
    print('Welcome,finally!')
  else:
    print('You cannot do it Leave it!')
else:
  print('Not correct')