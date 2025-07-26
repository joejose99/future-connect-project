def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target value.

    Parameters:
    arr (list): The sorted list of integers.
    target (int): The value to search for.

    Returns:
    int: The index of the target if found, else -1.
    """
    low = 0
    high = len(arr) - 1

    # Continue searching while the range is valid
    while low <= high:
    #while True:
        mid = (low + high) // 2  # Find the middle index

        # Check if mid is the target
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        else:
            high = mid - 1

    # Target not found
    return -1


# ----------------------------- Main Program -----------------------------

# Get user input for the array (must be sorted for binary search to work)
# user input should be in ascending order eg 1 2 3 4 10
arr = list(map(int, input("Enter space separated integers: ").split()))

# Get the target value to search
target = int(input("Enter the value to search: "))

# Call the binary search function with the input array and target value
result = binary_search(arr, target)

# Output the result
if result != -1:
    print(f"Target value {target} found at index {result}.")
else:
    print(f"Target value {target} not found in the array.")
