# This is a very simple game, feel free to encourage them to do more with it!

def beginning_scene():
  print("You're wandering in the woods at night, when you suddenly hear a noise.") 
  print("A huge spider comes out of the bush. Do you THROW your shoe or RUN away?")
  spider_choice = input("Enter your choice: ") 
  if spider_choice == "THROW":
    spider_attack() 
  elif spider_choice == "RUN":
    run_away()

def run_away():
  print("You run away, but you look back in horror as you realize the spider is much faster than you are.")
  print("The spider is the last thing you see before you die an unfortunate death.")
  print("YOU LOSE!")

def spider_attack():
  print("The spider dodges it and lunges at you!")
  print("You back up hurriedly and notice two objects on the ground. Do you pick up the ROCK or the STICK?")
  attack_choice = input("Enter your choice: ")
  if attack_choice == "ROCK":
    rock_spider() 
  elif attack_choice == "STICK":
    stick_spider()

def rock_spider():
  print("You throw the rock at the spider, and it thumps to the ground, dead.")
  print("YOU WIN!")

def stick_spider():
  print("The stick does nothing. Did you really expect a feeble stick to do anything?")
  print("The spider seems to laugh, then kills you.")
  print("YOU LOSE!")

beginning_scene()
