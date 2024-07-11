import game_logic
import FilesHandling as files

while(True):
    game_logic.menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        game_logic.game()
        print(game_logic.win_list)
        game_logic.win_list.clear()
    elif choice == "2":
        files.readFile()
    elif choice == "0":
        game_logic.end(choice)
    else:
        continue



