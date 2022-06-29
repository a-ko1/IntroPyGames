correct_answers = 0
total_answers = 5 

print("What language are you learning?") 
print("A. Python B. Java C. C++ D. Swift") 
answer1 = input("Enter your choice: ") 
if answer1 == "A":
  print("Correct!")
  correct_answers += 1
else:
  print("Wrong answer!")

print("What year is it?") 
print("A. 2021 B. 2022 C. 2023 D. 2024") 
answer1 = input("Enter your choice: ") 
if answer1 == "B":
  print("Correct!")
  correct_answers += 1
else:
  print("Wrong answer!")

print("Who is our current President?") 
print("A. Joe Biden B. Barack Obama C. Donald Trump D. Bill Clinton") 
answer1 = input("Enter your choice: ") 
if answer1 == "A":
  print("Correct!")
  correct_answers += 1
else:
  print("Wrong answer!")

print("What is the capital of the U.S.?") 
print("A. Chicago B. NYC C. Philadelphia D. Washington D.C.") 
answer1 = input("Enter your choice: ") 
if answer1 == "D":
  print("Correct!")
  correct_answers += 1
else:
  print("Wrong answer!")

print("Which casting function converts a number to a string?") 
print("A. int() B. float() C. str() D. print()") 
answer1 = input("Enter your choice: ") 
if answer1 == "C":
  print("Correct!")
  correct_answers += 1
else:
  print("Wrong answer!")

print("End of quiz!")
score = (correct_answers / total_answers) * 100
print("You got", correct_answers, "out of", total_answers, "correct!")
