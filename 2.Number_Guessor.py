import random

class number:
    
    best_score = 999999

    def __init__(self,min,max):
        self.count = 0
        self.num = random.randint(min,max)

    def guess(self,i):
        self.count += 1
        
        if i == self.num:
            print( f"Congo, You guessed, in {self.count}, attempts")
            if self.count < self.best_score:
                self.best_score = self.count
            return True
        
        elif i <= self.num - 10:
            print("Too Low")

        else:
            print("Too High")





mini = int(input("Give min and max please:"))
maxi = int(input())

n1 = number(mini,maxi)

while(True):

    i = int(input("Give ur guess"))

    if n1.guess(i) == True:
        break

        
