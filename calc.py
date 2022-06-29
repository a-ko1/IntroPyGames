# Simple, 4 operation calculator. Feel free to expand with more operations!
def addition(num1, num2):
  return num1 + num2

def subtraction(num1, num2):
  return num1 - num2

def multiplication(num1, num2):
  return num1 * num2

def division(num1, num2):
  return num1 / num2

# They can also use break statements to set this condition to False
continue_calculating = True

while continue_calculating:
  print("What do you want to do? ")
  print("A for addition, S for subtraction, M for multiplication, D for division")
  operation = input("Enter your choice: ")
  
  number1 = int(input("Enter a number: "))
  number2 = int(input("Enter another number: "))

  if operation == "A":
    print(addition(number1, number2))
  elif operation == "S":
    print(subtraction(number1, number2))
  elif operation == "M":
    print(multiplication(number1, number2))
  elif operation == "D":
    print(division(number1, number2))

  keep_calc = input("Do you want to calculate something else? Y / N ")
  if keep_calc == "Y":
    continue
  elif keep_calc == "N":
    continue_calculating = False

print("Thanks for using calculator!")
