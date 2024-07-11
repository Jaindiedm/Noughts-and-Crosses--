import os  # Module to interact with the operating system
import validat  # Module for input validation


cwd = os.getcwd()  # Gets the current working directory

def check_files(type):
    # Checks for session files in the current directory and returns a list of them
    session_files = []
    for filename in os.listdir(cwd):
        if filename.startswith("session") and filename.endswith(type):
            session_files.append(filename)
    return session_files

def save_data(win):
    # Saves the game session data to a file
    session_files = check_files(".txt")  # Gets the list of session files
    new_fil_name = ""  # Variable to store the new file name

    print(session_files)
    if len(session_files) == 0:
        # print("No session files found")
        new_fil_name = "session.txt"
    else:
        last_element = session_files[-1]
        if last_element[7] == ".":
            new_fil_name = "session2.txt"
        else:
            last = int(last_element[7]) + 1
            new_fil_name = f"session{last}.txt"
            print(new_fil_name)

    # Writes the game session data to the new file
    with open(new_fil_name, "w") as file:
        count1 = 0  # Counter for player 1 wins
        count2 = 0  # Counter for player 2 wins
        countTie = 0  # Counter for ties
        for i in win:
            if i == "play1":
                count1 += 1
            elif i == "play2":
                count2 += 1
            else:
                countTie += 1

        file.write(f"Player 1 win {count1} time/s for this session.\n")
        file.write(f"Player 2 win {count2} time/s for this session.\n")
        file.write(f"Draws for the session : {countTie}")


def readFile():
    # Reads and displays the contents of a selected session file
    session_files = check_files()  # Gets the list of session files
    opened = ""  # Variable to store the selected file name
    last_element = ""  # Variable to store the last session file name

    if len(session_files) == 0:
        print("No session files found")
    else:
        print("Available Sessions")
        for i in range(1, len(session_files) + 1):
            print(f"{i}. {session_files[i - 1]}")
        while True:
            openFile = input("Which session do you want to look at: ")
            passing = len(session_files) + 1
            openFile, validate = validat.validater(openFile, passing)  # Validates the user input
            if validate:
                opened = session_files[openFile - 1]  # Gets the selected file name
                last_element = opened
                if last_element[7] == ".":
                    last_element = 1
                else:
                    last_element = last_element[7]
                file = open(opened, "r")  # Opens the selected file
                with file:
                    print(f"Session {last_element}")
                    for line in file:
                        print(line, end="")
                    print("")
                    break

