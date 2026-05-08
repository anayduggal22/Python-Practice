import random

def rolling_dice():
    x = random.randint(1,6)
    y = random.randint(1,6)
    print(f"({x},{y})")



while(True):
    choice = input("Enter y/n to roll the dice:").lower()
    if(choice == 'y'):
        rolling_dice()
    
    else:
        break
    
    