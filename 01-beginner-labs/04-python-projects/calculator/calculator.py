
# Mathematical Operators

# User will select operator (+ - * /) and input two values when prompted.
# Value of two values will be calculated based on operand selected.

operand = input("Select operator: (+ - * /"))
num1 = float(input("Enter value 1: ")) # typecast as float for more complex calculations
num2 = float(input("Enter value 2: "))

if operand == "+":
  answer = num1 + num2
  print(round(answer, 3)) # round function added to round answer variable to 3 decimal places
elif operand == "-":
  answer = num1 - num2
  print(round(answer, 3))
elif operand == "*":
  answer = num1 * num2
  print(round(answer, 3))
elif operand == "/":
  answer = num1 + num2
  print(round(answer, 3))
else: 
  print(f"{operand} isn't a valid operator")


