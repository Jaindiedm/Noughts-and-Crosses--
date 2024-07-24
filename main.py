import game_logic  # Importing the game logic module
import FilesHandling as files  # Importing the file handling module

while(True):
    game_logic.menu()  # Display the game menu
    choice = input("Enter your choice: ")  # Get user choice
    if choice == "1":
        game_logic.game()  # Start the game
        # print(game_logic.win_list)  # Print the list of winners
        game_logic.win_list.clear()  # Clear the win list for a new game session
    elif choice == "2":
        files.readFile()  # View past game sessions
    elif choice == "0":
        game_logic.end(choice)  # Exit the program
    else:
        print("Enter valid input")
        continue  # Continue the loop if the input is invalid
