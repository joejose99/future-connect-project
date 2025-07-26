# Swap number using third variable.
x = int(input('Enter number 1:  '))  # Take first number from user
y = int(input('Enter number 2: '))   # Take second number from user

temp = x     # Store value of x in temp
x = y        # Assign value of y to x
y = temp     # Assign stored value of x (from temp) to y

print('After swapping \nNumber 1: ', x)  # Print swapped value of x
print('Number 2: ', y)                   # Print swapped value of y

# Swap number without using third variable.
x = int(input('Enter number 1:  '))  # Take first number again
y = int(input('Enter number 2: '))   # Take second number again

x, y = y, x  # Swap using Python's tuple unpacking (no third variable)

print('After swapping \nNumber 1: ', x)  # Print swapped value of x
print('Number 2: ', y)                   # Print swapped value of y
