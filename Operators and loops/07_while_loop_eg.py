# Guessing game

# generate a random integer between 1 and 100
import random
jackpot = random.randint(1,100)

guess = int(input('Please guess the number'))
counter = 1
while guess != jackpot:
  if guess < jackpot:
    print('Guess higher')
  else:
    print('Guess lower')

  guess = int(input('Please Guess the number'))
  counter += 1

else:
  print('correct guess')