def menu():
    print("1- Start Game")
    print("2- View past sessions")
    print("0- Exite")

def game():
    print("Welcome to the game/")
    play1 = input("Enter your name for player 1 : ")
    play2 = input("Enter your name for palyer 2 : ")
    game_logic(play1,play2)
    
    return play1, play2
    
def bord_indicator():
    for i in list1:
        count = 0
        for a in i:
            if a == 1 :
                print("   ",end="")
            else:
                print(f" {a} ",end="")
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
    turn = 1 
    while True:
        bord_indicator()
        if turn%2 == 1 :
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
        
        if check_win(turn):
            bord_indicator()
            break
        # else:
        #     continue
        turn += 1
        
def check_win(turn):
    
    if list1[0][0] == "X" and list1[0][1] == "X" and list1[0][2] == "X":
        win(turn)
        return True
    elif list1[1][0] == "X" and list1[1][1] == "X" and list1[1][2] == "X":
        win(turn)
        return True
    elif list1[2][0] == "X" and list1[2][1] == "X" and list1[2][2] == "X":
        win(turn)
        return True
    elif list1[0][0] == "O" and list1[0][1] == "O" and list1[0][2] == "O":
        win(turn)
        return True
    elif list1[1][0] == "O" and list1[1][1] == "O" and list1[1][2] == "O":
        win(turn)
        return True
    elif list1[2][0] == "O" and list1[2][1] == "O" and list1[2][2] == "O":
        win(turn)
        return True
    elif list1[0][0] == "X" and list1[1][1] == "X" and list1[2][2] == "X":
        win(turn)
        return True
    elif list1[0][0] == "O" and list1[1][1] == "O" and list1[2][2] == "O":
        win(turn)
        return True
    elif list1[0][2] == "O" and list1[1][1] == "O" and list1[2][0] == "O":
        win(turn)
        return True
    elif list1[0][2] == "X" and list1[1][1] == "X" and list1[2][0] == "X":
        win(turn)
        return True
    


def win(num):
    if num ==1 :
        print("Player 1 wins")
    else:
        print("Player 2 wins")
    
    
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
        # check_win()
    elif choice == "2":
        pass
    elif choice == "0":
        print("Exiting Program")
        exit()
    else:
        continue



