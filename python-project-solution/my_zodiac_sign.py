# Import necessary modules
import datetime
import csv
import pandas

# Dictionary to store user data
Dictionary1 = {}

# Function to take valid day input from the user
def takeUserDay():
    try:
        day = int(input('Enter day: '))
        
        # Ensure day is within valid range
        if day <= 0 or day > 31:
            print('Enter a valid day!!! ')
            return takeUserDay()
        else:
            return day
    except:
        print('ERROR: Only Numbers are accepted!')
        return takeUserDay()

# Function to take and convert month input into a numeric month
def takeUserMonth():
    month = input('Enter month: ')
    
    # Mapping different formats of each month to its corresponding number
    if month in ['January', '1', 'Jan', 'january', 'jan', '01']:
        return 1
    elif month in ['February', '2', 'Feb', 'february', 'feb', '02']:
        return 2
    elif month in ['March', '3', 'Mar', 'march', 'mar', '03']:
        return 3
    elif month in ['April', '4', 'Apr', 'april', 'apr', '04']:
        return 4
    elif month in ['May', '5', 'may', '05']:
        return 5
    elif month in ['June', '6', 'june', '06']:
        return 6
    elif month in ['July', '7', 'july', '07']:
        return 7
    elif month in ['August', '8', 'Aug', 'august', 'aug', '08']:
        return 8
    elif month in ['September', '9', 'Sept', 'september', 'sept', '09']:
        return 9
    elif month in ['October', '10', 'Oct', 'october', 'oct']:
        return 10
    elif month in ['November', '11', 'Nov', 'november', 'nov']:
        return 11
    elif month in ['December', '12', 'Dec', 'december', 'dec']:
        return 12
    else:
        print('ERROR: Enter a valid month ')
        return takeUserMonth()

# Function to take a valid year input
def takeUserYear():
    try:
        year = int(input('Enter year: '))
        
        if year <= 0:
            print('ERROR: Year must be positive')
            return takeUserYear()
        elif year % 4 == 0:
            print('Leap year!')
            return year
        else:
            return year
    except:
        print('ERROR: Enter Numerical Value Only')
        return takeUserYear()

# Function to calculate Zodiac sign based on day and month
def calculateSign(day, month):
    if month == 12:
        return 'Sagittarius' if day < 22 else 'Capricorn'
    elif month == 1:
        return 'Capricorn' if day < 20 else 'Aquarius'
    elif month == 2:
        return 'Aquarius' if day < 19 else 'Pisces'
    elif month == 3:
        return 'Pisces' if day < 21 else 'Aries'
    elif month == 4:
        return 'Aries' if day < 20 else 'Taurus'
    elif month == 5:
        return 'Taurus' if day < 21 else 'Gemini'
    elif month == 6:
        return 'Gemini' if day < 21 else 'Cancer'
    elif month == 7:
        return 'Cancer' if day < 23 else 'Leo'
    elif month == 8:
        return 'Leo' if day < 23 else 'Virgo'
    elif month == 9:
        return 'Virgo' if day < 23 else 'Libra'
    elif month == 10:
        return 'Libra' if day < 23 else 'Scorpio'
    elif month == 11:
        return 'Scorpio' if day < 22 else 'Sagittarius'

# Function to create a full date object
def takeDate(year, month, day):
    date1 = datetime.date(year, month, day)
    print('DOB: ', date1)
    return date1

# Function to ask if the user wants to continue
def repeatQuestion():
    #Finder = input('Do you want to find any other Zodiac sign(yes/no): ')
    
    #return Finder.lower() == 'yes'
   
    while True:
        Finder = input('Do you want to find another Zodiac sign? (yes/no): ').strip().lower()
        if Finder in ['yes', 'y']:
            return True
        elif Finder in ['no', 'n']:
            print("Thank you! Exiting the program.")
            
            return False
            
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

# Function to gather full input from a user and store in dictionary
def UserInput(count):
    userName = input('Enter the name of the user: ')
    userYear = takeUserYear()
    userMonth = takeUserMonth()
    userDate = takeUserDay()
    
    fullDate = takeDate(userYear, userMonth, userDate)
    yourSign = calculateSign(userDate, userMonth)
    
    print(userName, "your Zodiac sign is:", yourSign)
    
    # Store user data in the dictionary
    Dictionary1[count] = {
        'FullName': userName,
        'DateOfBirth': str(fullDate),
        'ZodiacSign': yourSign
    }

    print(Dictionary1[count])

# Placeholder (not used)
def SavetoPandas():
    pass

# ------------------------- Main Program -------------------------

if __name__ == '__main__':
    Repeat = True
    Count = 1
    
    # Keep collecting input while user agrees
    while Repeat:
        UserInput(Count)
        Count += 1
        Repeat = repeatQuestion()
        
    
        

    # Convert collected data to pandas DataFrame
    df = pandas.DataFrame(data=Dictionary1)

    # Ask user for a filename and save to CSV
    fileName = input('Please enter file Name: ')
    df.to_csv(fileName + '.csv', index=True)
    print(df)
