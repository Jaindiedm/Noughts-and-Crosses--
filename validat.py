def validater(num,endpoint):
    if num.isdigit():
        num = int(num)
        if num < endpoint and num > 0:
            return num,True
        else:
            print(f"Enter number between 1 and {endpoint}.")
            return num,False
    else:
        print("Invalid input")
        return num,False