import random

number = random.randint(1, 10) # Or have them choose their own number
guesses_taken = 0 

# Feel free to set the number of guesses
while guesses_taken < 3:
  guesses_taken += 1
  guess = int(input("Enter a number from 1 to 10: "))
  if guess == number:
    print("You win! The number was", number)
    break
  elif guess > number:
    print("Too high!")
  elif guess < number:
    print("Too low!")

if guesses_taken == 3 and guess != number:
  print("You ran out of guesses! The number was", number)
else:
  print("You won in", guesses_taken, "guesses!")

