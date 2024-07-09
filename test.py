def menu():
    print("1- Start Game")
    print("2- View past sessions")
    print("0- Exite")

def game():
    print("Welcome to the game")
    play1 = input("Enter your name for player 1 : ")
    play2 = input("Enter your name for palyer 2 : ")
    
    return play1, play2
    
def bord_indicator():
    for i in list1:
        count = 0
        for a in i:
            if a == 1 :
                print("  h ")
            else:
                print(a)
            if count < 2:
                print(" | ")
                count += 1 
            else:
                continue
        # print("")
                

print("Welcome to Tic Tac Toe")

global list1 
list1 = [[1 for x in range(3)] for y in range(3)]

while(True):
    menu()
    bord_indicator()
    choice = input("Enter your choice: ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "0":
        print("Exiting Program")
        exit()
    else:
        continue



