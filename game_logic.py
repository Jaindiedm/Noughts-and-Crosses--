import FilesHandling as files  # Handles file operations
import validat  # Handles input validation
import HandleHtml

def menu():
    # Displays the main menu
    print("1- Start Game")
    print("2- View past sessions")
    print("0- Exit")

def bord_indicator():
    # Displays the current game board
    for i in game_list:
        count = 0
        for a in i:
            if a == 1:
                print("   ", end="")
            else:
                print(f" {a} ", end="")
            if count < 2:
                print(" | ", end="")
                count += 1 
            else:
                continue
        print("")
        print("---------------")

def tic_tac_toaValidate(tic):
    # Validates player input for 'X' or 'O'
    if tic.lower() == "x" or tic.lower() == "o":
        return True
    else:
        print("Invalid input, Enter 'O' or 'X'")
        return False

def game_logic(play1, play2, play1Tic, play2Tic):
    # Main game logic, handling turns, input validation, board updates, and win/tie checks
    turn = 1  # Tracks the number of turns
    global game_list
    game_list = [[1 for x in range(3)] for y in range(3)]  # Initializes the game board with default values
    while True:
        bord_indicator()
        if turn % 2 == 1:
            print(f"Player 1 turn ({play1})")
        else:
            print(f"Player 2 turn ({play2})")
        
        while True:
            row = input("Enter the row number: ")
            row, validate = validat.validater(row, 4)  # Validates the row input
            if validate:
                break
        
        while True:
            col = input("Enter the column number: ")
            col, validate = validat.validater(col, 4)  # Validates the column input
            if validate:
                break
        
        if game_list[row - 1][col - 1] == 1:
            # Updates the game board with the player's move
            if turn % 2 == 1:
                game_list[row - 1][col - 1] = play1Tic.upper()
            else:
                game_list[row - 1][col - 1] = play2Tic.upper()
        else:        
            print("This cell is already occupied. Try again.")
            continue
        
        if turn > 2:
            # Checks for a win or tie condition after the third turn
            if check_win(turn) or tie():
                bord_indicator()
                if play_again():
                    turn += 1
                    game_list = [[1 for x in range(3)] for y in range(3)]  # Resets the game board
                    continue
                else:
                    IsNeedToWriteFile()
                    break

        turn += 1

def tie():
    # Checks if the game is a tie
    count = 0
    for i in game_list:
        if 1 not in i:
            count += 1
        else:
            continue
    if count == 3:
        print("It's a tie!")
        win_list.append("tie")  # Records the tie result
        return True
    else:
        return False

def check_win(turn):
    # Checks for a winning condition
    listx = ["X", "X", "X"]  # Winning condition for player with 'X'
    listo = ["O", "O", "O"]  # Winning condition for player with 'O'
    if game_list[0][0] == "X" and game_list[1][1] == "X" and game_list[2][2] == "X":
        win(turn)
        return True
    elif game_list[0][0] == "O" and game_list[1][1] == "O" and game_list[2][2] == "O":
        win(turn)
        return True
    elif game_list[0][2] == "O" and game_list[1][1] == "O" and game_list[2][0] == "O":
        win(turn)
        return True
    elif game_list[0][2] == "X" and game_list[1][1] == "X" and game_list[2][0] == "X":
        win(turn)
        return True
    elif listx in game_list or listo in game_list:
        win(turn)
        return True
    for i in range(0, 3):
        countx = 0 
        countO = 0
        for a in range(0, 3):
            if game_list[a][i] == "X": 
                countx += 1
                if countx == 3:
                    win(turn)
                    return True
            elif game_list[a][i] == "O":
                countO += 1
                if countO == 3:
                    win(turn)
                    return True
    if countO == 3 or countx == 3:
        win(turn)
        return True
    
    return False

def play_again():
    # Prompts players to decide whether to play again
    while True:
        play = input("Do you want to play again? (Y/N): ")
        if play.upper() == "Y":
            global game_list
            game_list = [[1 for x in range(3)] for y in range(3)]  # Resets the game board
            return True
        elif play.upper() == "N":
            return False
        else:
            print("Invalid Input. Try again.")
            continue

def end(input):
    # Ends the game if the input is "0"
    if input == "0":
        IsNeedToWriteFile()
        print("Exiting Program")
        exit()
    
    

def IsNeedToWriteFile():
    # Saves the game result if there are recorded wins
    if len(win_list) != 0:
        files.save_data(win_list)
        HandleHtml.saveDataOnHTML(win_list)
    else:
        print("File not created, Game not finish")

def win(num):
    # Announces the winner and records the win
    if num % 2 == 1:
        print("-------------------")
        print("")
        print("Player 1 wins")
        print("")
        print("-------------------")
        win_list.append("play1")  # Records win for player 1
    else:
        print("-------------------")
        print("")
        print("Player 2 wins")
        print("")
        print("-------------------")
        win_list.append("play2")  # Records win for player 2

def game():
    # Initializes the game by getting player names and their chosen symbols
    print("Welcome to the game")
    play1 = input("Enter your name for player 1: ")
    end(play1)
    play1Tic = ""  # Symbol chosen by player 1
    play2Tic = ""  # Symbol assigned to player 2
    while True:
        tic = input("Enter Noughts and Crosses: ")
        if tic_tac_toaValidate(tic):
            play1Tic = tic
            if play1Tic.lower() == "x":
                play2Tic = "O"
            else:
                play2Tic = "X"
            break
    play2 = input("Enter your name for player 2: ")
    end(play2)
    game_logic(play1, play2, play1Tic, play2Tic)

global win_list
win_list = []  # List to record game outcomes (wins and ties)
