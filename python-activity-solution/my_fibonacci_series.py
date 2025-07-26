while True:
    user_input = input("Enter the length of the Fibonacci series (or 'q' to quit): ")
    
    if user_input.lower() in ['q', 'quit']:
        print("Exiting the program. Goodbye!")
        break

    if not user_input.isdigit():
        print("Invalid input! Please enter a positive integer or 'q' to quit.")
        continue

    n = int(user_input)

    # define the first two numbers in the series
    a, b = 0, 1
    count = 0

    if n <= 0:
        print("Enter a positive integer!")
    elif n == 1:
        print("Fibonacci series up to", n, ":", a)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(a)
            nth = a + b
            a = b
            b = nth
            count += 1
