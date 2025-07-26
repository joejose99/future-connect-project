# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract second number from first
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide first number by second
def divide(x, y):
    return x / y


# Display operation choices to the user
print("SELECT OPERATION")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Infinite loop to allow multiple calculations until user exits
while True:

    # Get user's choice
    choice = input("ENTER CHOICE: ")

    # Validate the input choice
    if choice in ('1', '2', '3', '4'):
        try:
            # Get numbers from the user and convert to float
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            # Handle invalid number input
            print("INVALID INPUT. \n Please enter a number between 1-4: ")
            continue

        # Perform addition
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        # Perform subtraction
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        # Perform multiplication
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        # Perform division
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # Ask user if they want to continue
        New_calculation = input("Do you want to do any other calculation (yes/no): ")
        if New_calculation == "no":
            break  # Exit loop if user types 'no'
    else:
        # Handle invalid operation choice
        print("Invalid Input")
