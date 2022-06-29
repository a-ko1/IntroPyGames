import random

ball_answer = random.randint(1, 7)

question = input("Type a question for the magic 8 ball: ")

if ball_answer == 1:
  print("It is certain.")
elif ball_answer == 2:
  print("Signs point to yes.")
elif ball_answer == 3:
  print("Reply hazy, try again")
elif ball_answer == 4:
  print("Concentrate and ask again.")
elif ball_answer == 5:
  print("Don't count on it.")
elif ball_answer == 6:
  print("My sources say no.")
elif ball_answer == 7:
  print("Outlook good.")
