

# This function subtracts two numbers
def miles(x):
    return x * 1.609344

def kilometers(x):
    return x * 0.621371
print("Write your distance in next value:")
print("1.Kilometers (Answer will be in miles)")
print("2.Miles (Answer will be in kilometers)")

while True:
    # take input from the user
    choice = input("Enter choice(1/2): ")
    if choice in ('1', '2'):
        try:
            num1 = float(input("Enter value of your distance: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "*", "0.62" "=", "%.2f" % kilometers(num1), "miles")
        elif choice == '2':
            print(num1, "*", "1.609" "=", "%.2f" % miles(num1), "kilometers")
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")