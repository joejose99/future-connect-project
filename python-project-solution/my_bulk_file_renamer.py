import os  # Import the os module to interact with the operating system

# Ask the user to input the directory path
path = input("Enter path: ")

# Print the entered path (for debugging or confirmation)
print(path)

# Print list of files/folders in the specified path
print(os.listdir(path))  # Reminder: directory path must end with '/' or '\\' depending on OS

# Main function that renames files in the given path
def main():
    i = 1  # Counter for new file names
    for filename in os.listdir(path):  # Iterate over all files in the directory
        new_name = path + str(i) + '.jpg'  # Construct the new file name with incremented number
        old_name = path + filename  # Get the full original file path
        os.rename(old_name, new_name)  # Rename the file
        i += 1  # Increment counter for next file

# Call the main function
main()
