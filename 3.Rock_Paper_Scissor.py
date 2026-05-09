import random

def Generate():

    num = random.randint(1,3)

    if num == 1:
        return 'r'
    elif num == 2:
        return 'p'
    else:
        return 's'
    

computer = 0
human = 0

while(True):

    if computer >= 2:
        print("Computer Wins!!")
        break
    elif human >= 2:
        print("Player Wins!!")
        break

    h = input("Choose Between r/p/s")
    c = Generate()

    if h == 'r' and c == 'r':
        print("Tie")
    elif h == 'r' and c == 'p':
        print("Computer Gets 1 Point")
        computer += 1
    elif h == 'r' and c == 's':
        print("Human Gets 1 Point")
        human += 1
    elif h == 'p' and c == 'r':
        print("Human Gets 1 Point")
        human += 1
    elif h == 'p' and c == 'p':
        print("Tie")
    elif h == 'p' and c == 's':
        print("Computer Gets 1 Point")
        computer += 1
    elif h == 's' and c == 'r':
        print("Computer Gets 1 Point")
        computer += 1
    elif h == 's' and c == 'p':
        print("Human Gets 1 Point")
        human += 1
    elif h == 's' and c == 's':
        print("Tie")
    else:
        print("Invalid!!")
        break

    choice = input("Do you want to still play y/n")

    if choice == 'n':
        break

    