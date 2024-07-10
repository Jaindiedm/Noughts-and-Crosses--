import test as files
import validat

def menu():
    print("1- Start Game")
    print("2- View past sessions")
    print("0- Exit")

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
        
def tic_tac_toaValidate(tic):
    if tic.lower() == "x" or tic.lower() == "o":
        return True
    else:
        print("Invalid input , Enter 'O' or 'x'")
        return False
                
def game_logic(play1,play2,play1Tic,play2Tic):
    turn = 1 
    global list1
    list1 = [[1 for x in range(3)] for y in range(3)]
    while True:
        bord_indicator()
        if turn%2 == 1 :
            print(f"Player 1 turn ({play1})")
        else :
            print(f"Player 2 turn ({play2})")
            
        while True:
            row = input("Enter the row number : ")
            row,validate = validat.validater(row,4)
            if validate :
                break
        
        while True:
            col = input("Enter the column number : ")
            col,validate = validat.validater(col,4)
            if validate :
                break
            
        if list1[row-1][col-1] == 1:
            if turn%2 == 1:
                list1[row-1][col-1] = play1Tic.upper()
            else:
                list1[row-1][col-1] = play2Tic.upper()
                
        else:        
            print("This cell is already occupied. Try again.")
            continue
        if turn >2:
            if  check_win(turn) or tie():
                bord_indicator()
                if play_again():
                    turn += 1
                    list1 = [[1 for x in range(3)] for y in range(3)]
                    continue
                else:
                    IsNeedToWriteFile()
                    break

        turn += 1

def tie():
    count = 0
    for i in list1:
        if 1 not in i:
            count += 1
        else:
            continue
    if count == 3 :
        print("It's a tie!")
        win_list.append("tie")
        return True
    else:
        return False
                
def check_win(turn):
    

    listx = ["X","X","X"]
    listo = ["O","O","O"]
    if list1[0][0] == "X" and list1[1][1] == "X" and list1[2][2] == "X":
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
    elif listx in list1 or listo in list1:
        win(turn)
        return True
    for i in range(0,3):
        countx=0 
        countO=0
        for a in range(0,3):
            if list1[a][i] == "X": 
                countx += 1
                if countx == 3:
                    win(turn)
                    return True
            elif list1[a][i] =="O":
                countO += 1
                if countO ==3 :
                    win(turn)
                    return True
    if countO == 3 or countx == 3:
        win(turn)
        return True
    

    return False
    
def play_again():
    while True:
        play = input("Do you want to play again? (Y/N) : ")
        if play.upper() == "Y":
            global list1
            list1 = [[1 for x in range(3)] for y in range(3)]
            return True
        elif play.upper() == "N":
            return False
        else:
            print("Invalid Input. Try again.")
            continue
def end(input):
    if input == "0":
        IsNeedToWriteFile()
        print("Exiting Program")
        exit()

def IsNeedToWriteFile():
    if len(win_list) != 0:
        files.save_data(win_list)
    else:
        print("File not created , Game not finish")

def win(num):
    if num%2 ==1 :
        print("Player 1 wins")
        win_list.append("play1")
    else:
        print("Player 2 wins")
        win_list.append("play2")
 
def game():
    print("Welcome to the game/")
    play1 = input("Enter your name for player 1 : ")
    end(play1)
    play1Tic = ""
    play2Tic =""
    while True:
        tic = input("Enter Noughts and Crosses : ")
        if tic_tac_toaValidate(tic):
            play1Tic = tic
            if play1Tic.lower() == "x":
                play2Tic = "O"
            else:
                play2Tic = "X"
            break
    play2 = input("Enter your name for palyer 2 : ")
    end(play2)
    game_logic(play1,play2,play1Tic,play2Tic)
       
print("Welcome to Tic Tac Toe")

global win_list
win_list = []

while(True):
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        game()
        print(win_list)
        win_list.clear()
    elif choice == "2":
        files.readFile()
    elif choice == "0":
        end(choice)
    else:
        continue



