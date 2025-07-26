# Define a function to swap case of each character
def my_swap_case(swap):
    string = ''  # Initialize an empty string to store the result

    # Iterate over each character in the input string
    for char in swap:
        # If character is lowercase, convert to uppercase
        if char.islower():
            string += char.upper()
        # Otherwise, convert to lowercase (this handles uppercase and other cases)
        else:
            string += char.lower()
        
    return string  # Return the modified string

# Main block to run the code
if __name__ == '__main__':
    swap = input('Enter string: ')           # Take input from user
    result = my_swap_case(swap)                 # Call function to swap case
    print('Swapped string: ' + result)       # Output the result
