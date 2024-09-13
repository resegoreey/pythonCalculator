def calculator():
  print("Choose the operation you want to use ")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")

  user_input = input("Choose from above(1-4): ")
  num1 = int(input("first number?: "))
  num2 = int(input("second number?: "))

  if user_input == "1":
    print(num1 + num2)
  elif user_input == "2":
    print(num1 - num2)
  elif user_input == "3":
    print(num1 * num2)
  elif user_input == "4":
    if num2 != 0:
      print(num1 / num2)
    else:
      print("You can't divide by zero!")
  else:
    print("Invalid")

calculator()

