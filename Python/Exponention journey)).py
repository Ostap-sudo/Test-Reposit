def exponention (x,y):
    return x**y
while True:
    choice = input("Ready for exponention journey?))(yes/no): ")

    # check if choice is one of the four options
    if choice  == "yes":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 'yes':
            print(num1, "**", num2,"=", exponention(num1, num2))
        elif choice == "no":
            break
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")