import random

# Display the game rules
print('ROCK PAPER SCISSORS GAME!\n' +
      'Game Rules:\n' +
      'Rock vs Paper --> Paper wins\n' +
      'Rock vs Scissors --> Rock wins\n' +
      'Paper vs Scissors --> Scissors wins\n')

while True:
    # Prompt user to enter their choice
    print('Enter your choice:\n 1 - Rock\n 2 - Paper\n 3 - Scissors')
    choice = int(input('Enter your choice: '))

    # Validate user input
    while choice < 1 or choice > 3:
        choice = int(input('Enter a valid choice (1-3): '))

    # Map number to corresponding choice name
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('User choice is:', choice_name)
    print('Now it\'s computer\'s turn!')

    # Generate computer's choice (different from user's to avoid immediate draw)
    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # Map computer's choice to choice name
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is:", comp_choice_name)
    print(f"{choice_name} VS {comp_choice_name}")

    # Determine winner
    if choice == comp_choice:
        result = 'Draw'
        print('Draw')
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        result = 'Paper'
        print('Paper wins: ', end='')
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = 'Rock'
        print('Rock wins: ', end='')
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        result = 'Scissors'
        print('Scissors wins: ', end='')

    # Show result message
    if result == 'Draw':
        print("<== It's a tie ==>")
    elif result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    # Ask user if they want to play again
    answer = input('Do you want to play again? (Y/N): ').strip().lower()
    if answer == 'n':
        print("Thanks for playing!")
        break
