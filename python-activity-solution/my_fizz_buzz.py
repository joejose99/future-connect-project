# Loop through numbers from 1 to 100 (inclusive)
for i in range(1, 101):
    
    # If the number is divisible by both 3 and 5 (i.e., 15), print 'FizzBuzz'
    if i % 15 == 0:
        print('FizzBuzz')
        
    # If the number is divisible only by 3, print 'Fizz'
    elif i % 3 == 0:
        print('Fizz')
        
    # If the number is divisible only by 5, print 'Buzz'
    elif i % 5 == 0:
        print('Buzz')
        
    # If none of the above, print the number itself
    else:
        print(i)
