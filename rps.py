game_being_played = True
while game_being_played:
  print("Welcome to Rock, Paper, Scissors!")
  print("PLAYER 1, Enter R for rock, S for scissors, P for paper")        
  player1_move = input("Enter your choice: ")
  print("PLAYER 2, Enter R for rock, S for scissors, p for paper")
  player2_move = input("Enter your choice: ")

  # If player 1 chooses rock
  if player1_move == "R": 
    # and player 2 chooses scissors
    if player2_move == "S":
      print("PLAYER 1 wins! ROCK beats SCISSORS.")
    # and player 2 chooses paper
    elif player2_move == "P":
      print("PLAYER 2 wins! PAPER beats ROCK")

  # If player 1 chooses scissors
  if player1_move == "S": 
    # and player 2 chooses rock
    if player2_move == "R":
      print("PLAYER 2 wins! ROCK beats SCISSORS.")
    # and player 2 chooses paper
    elif player2_move == "P":
      print("PLAYER 1 wins! SCISSORS beats PAPER")

  # If player 1 chooses paper
  if player1_move == "P": 
    # and player 2 chooses rock
    if player2_move == "R":
      print("PLAYER 1 wins! PAPER beats ROCK.")
    # and player 2 chooses scissors
    elif player2_move == "S":
      print("PLAYER 2 wins! SCISSORS beats PAPER")

  play_again = input("Do you want to play again? Y/N ")
  if play_again == "Y":
    continue 
  elif play_again == "N":
    game_being_played = False

print("Thank you for playing Rock, Paper, Scissors!")
