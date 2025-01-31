def addition(num1, num2):
  return num1 + num2

def subtraction(num1, num2):
  return num1 - num2

def multiplication(num1, num2):
  return num1 * num2

def division(num1, num2):
  return num1 / num2

def main():
  new_game = True
  while new_game:
    print("-----------------------------------")
    print("Welcome to Simple Python Calculator")
    print("-----------------------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("-----------------------------------")

    # valid number one
    valid_number_one = True
    while valid_number_one:
      number_one = input("Enter your first number: ")
      try:
        number_one = float(number_one)
        valid_number_one = False
      except ValueError:
        print("Please enter a valid number!")

    # valid the operator
    valid_operator = True
    while valid_operator:
      operators = ["1", "2", "3", "4"]
      try:
        user_input = input("Choose a Operator (1/2/3/4): ")
        if user_input in operators:
          valid_operator = False
      except ValueError:
          print("Please select a valid operator")

    # valid number two
    valid_number_two = True
    while valid_number_two:
      number_two = input("Enter your second number: ")
      try:
        number_two = float(number_two)
        valid_number_two = False
      except ValueError:
        print("Please enter a valid number!")

    # calculation
    if user_input == "1":
      total = addition(number_one, number_two)
      print("--------------------------------------")
      print(f"{number_one} + {number_two} = {total}")
      print("--------------------------------------")
      play_again = input("Do you want to play again? (Y / N): ").upper()
      if play_again != "Y":
        new_game = False

    elif user_input == "2":
      total = subtraction(number_one, number_two)
      print("--------------------------------------")
      print(f"{number_one} - {number_two} = {total}")
      print("--------------------------------------")
      play_again = input("Do you want to play again? (Y / N): ").upper()
      if play_again != "Y":
        new_game = False

    elif user_input == "3":
      total = multiplication(number_one, number_two)
      print("--------------------------------------")
      print(f"{number_one} * {number_two} = {total}")
      print("--------------------------------------")
      play_again = input("Do you want to play again? (Y / N): ").upper()
      if play_again != "Y":
        new_game = False

    else:
      total = division(number_one, number_two)
      print("--------------------------------------")
      print(f"{number_one} / {number_two} = {total:.2f}")
      print("--------------------------------------")
      play_again = input("Do you want to play again? (Y / N): ").upper()
      if play_again != "Y":
        new_game = False

if __name__ == "__main__":
    main()


