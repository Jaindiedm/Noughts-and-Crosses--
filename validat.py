def validater(num, endpoint):
    # Check if the input 'num' is a digit
    if num.isdigit():
        # Convert 'num' to an integer
        num = int(num)
        # Check if 'num' is within the valid range
        if num < endpoint and num > 0:
            return num, True
        else:
            # Print an error message if 'num' is out of range
            print(f"Enter number between 1 and {endpoint-1}.")
            return num, False
    else:
        # Print an error message if 'num' is not a valid digit
        print("Invalid input")
        return num, False