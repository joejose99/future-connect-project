# Number guessing game
import random  # Import the random module for generating random numbers

# Generate a random number between 0 and 100
number = random.randint(0, 100)
print('Number: ', number)  # Print the number (for debugging; remove in real gameplay)

trials = 5  # Number of attempts allowed
message = 'You Lost!'  # Default message if the player fails to guess correctly

# Game loop: runs while player still has trials left
while trials > 0:
    print(f'{trials} attempt left.')  # Show remaining attempts
    trials -= 1  # Decrease the trial count after each attempt
    user_input = int(input('Enter Number: '))  # Get user input and convert to integer

    if user_input == number:
        message = 'You Won!'  # Change message if guessed correctly
        break  # Exit the loop if the correct number is guessed
    else:
        print('Try again!')  # Inform the user to try again

# Print the final result message
print(message)
