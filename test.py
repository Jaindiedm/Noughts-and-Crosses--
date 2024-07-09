def menu():
    print("1- Start Game")
    print("2- View past sessions")
    print("0- Exite")

def game():
    print("Welcome to the game/")
    play1 = input("Enter your name for player 1 : ")
    play2 = input("Enter your name for palyer 2 : ")
    bord_indicator()
    game_logic(play1,play2)
    
    return play1, play2
    
def bord_indicator():
    for i in list1:
        count = 0
        for a in i:
            if a == 1 :
                print("   ",end="")
            else:
                print(a)
            if count < 2:
                print(" | ",end="")
                count += 1 
            else:
                continue
        print("")
        print("---------------")
        
def validater(num):
    if num.isdigit():
        num = int(num)
        if num < 4 and num > 0:
            return num,True
        else:
            print("Enter number between 1 and 3.")
            return num,False
    else:
        print("Invalid input")
        return num,False

def tic_tac_toaValidate(tic):
    if tic.lower() == "x" or tic.lower() == "o":
        return True
    else:
        print("Invalid input , Enter 'O' or 'x'")
        return False
                
def game_logic(play1,play2):
    while True:
        turn = 1 
        if turn == 1 :
            print(f"Player 1 turn ({play1})")
        else :
            print(f"Player 2 turn ({play2})")
            
        while True:
            row = input("Enter the row number : ")
            row,validate = validater(row)
            if validate :
                break
        
        while True:
            col = input("Enter the column number : ")
            col,validate = validater(col)
            if validate :
                break
            
        if list1[row-1][col-1] == 1:
            while True:
                tic = input("Enter Noughts and Crosses : ")
                if tic_tac_toaValidate(tic):
                    list1[row-1][col-1] = tic.upper()
                    break
                else:
                    continue
        else:        
            print("This cell is already occupied. Try again.")
            continue
        
        
        



print("Welcome to Tic Tac Toe")

global list1 
list1 = [[1 for x in range(3)] for y in range(3)]

while(True):
    menu()
    # bord_indicator()
    # break
    choice = input("Enter your choice: ")
    if choice == "1":
        game()
    elif choice == "2":
        pass
    elif choice == "0":
        print("Exiting Program")
        exit()
    else:
        continue



