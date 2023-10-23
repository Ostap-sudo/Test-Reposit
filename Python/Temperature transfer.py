import math# This function adds two numbers
def celsius(x):
    return x

# This function subtracts two numbers
def kelvin(x):
    return x + 273.15

def fahrenheit(x):
    return x *1.8 + 32
print("Write value in Celsius scale")
print("Select your temperature type.")
print("1.Kelvin")
print("2.Fahrenheit")

while True:
    # take input from the user
    choice = input("Enter choice(1/2): ")
    if choice in ('1', '2'):
        try:
            num1 = float(input("Enter temperature in celcius: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", "273" "=", kelvin(num1))
        elif choice == '2':
            print(num1, "*", "1.8 + 32" "=", fahrenheit(num1))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")