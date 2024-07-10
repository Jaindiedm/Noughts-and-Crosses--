import os
import validat

# Get the current working directory
cwd = os.getcwd()

# Initialize an empty list to store session file names

def check_files():
  session_files = []
  for filename in os.listdir(cwd):
    # Check if the filename starts with "session" and ends with ".txt"
    if filename.startswith("session") and filename.endswith(".txt"):
      session_files.append(filename)  # Add filename to the list
  return session_files

def save_data(win):
  
  session_files = check_files()
  new_fil_name = ""
  # Print the list of session files
  print(session_files)
  if len(session_files) == 0:
    print("No session files found")
    new_fil_name = "session.txt"
  else:
    last_element = session_files[-1]
    if last_element[7] == ".":
      new_fil_name = "session2.txt"
    else:
      last = int(last_element[7])+1
      new_fil_name = f"session{last}.txt"
      print(new_fil_name)


  # Open the file in write mode ("w")
  with open(new_fil_name, "w") as file:
    # Write text to the file
    count1 = 0
    count2 = 0
    countTie =0
    for i in win :
      if i == "play1":
        count1 +=1
      elif i == "play2":
        count2 +=1
      else:
        countTie +=1
    file.write(f"Player 1 win {count1} time/s for this session.\n")
    file.write(f"Player 2 win {count2} time/s for this session.\n")
    file.write(f"Draws for the session : {countTie}")

def readFile():
  session_files = check_files()
  opened =""
  last_element=""
  if len(session_files) == 0:
    print("No session files found")
  else:
    print("available Sessions")
    for i in range(1,len(session_files)+1):
      print(f"{i}. {session_files[i-1]}")
    while True:
      openFile = input("Which session do you want to look: ")
      passing = len(session_files)+1
      openFile,validate = validat.validater(openFile,passing)
      if validate:
        opened = session_files[openFile-1]
        last_element = opened
        if last_element[7] == ".":
          last_element=1
        else:
          last_element = last_element[7]
        file = open(opened,"r")
        with file:
          print(f"Session {last_element}")
          for line in file:
            print(line,end="")
          print("")
          break



# readFile()


# list1 = ["play2","play1","play1","play2","play1","play2","play1","play1","tie",'tie']

# save_data(list1)