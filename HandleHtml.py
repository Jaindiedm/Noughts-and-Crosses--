import FilesHandling as files

def saveDataOnHTML(win):
    # Open the file in the write mode
        # Saves the game session data to a file
    session_files = files.check_files(".html")  # Gets the list of session files
    new_fil_name = ""  # Variable to store the new file name
    if len(session_files) == 0:
        # print("No session files found")
        new_fil_name = "session.html"
    else:
        last_element = session_files[-1]
        if last_element[7] == ".":
            new_fil_name = "session2.html"
        else:
            last = int(last_element[7]) + 1
            new_fil_name = f"session{last}.html"

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
        
        file.write(f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home</title>
    </head>
    <body>
        <h1>Noughts and Crosses Game Results</h1>\n""")
        if count1 != 0:
            file.write(f"<h1>Player 1 win {count1} time/s for this session.</h1>\n")
        if count2 !=0:
            file.write(f"<h1>Player 2 win {count2} time/s for this session.</h1>\n")
        if countTie !=0:
            file.write(f"<h1>Tie {countTie} time/s for this session.</h1>\n")
        file.write("""</body>
</html>
""")

    print("Session files created successfully")


