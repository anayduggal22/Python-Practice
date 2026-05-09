with open("anay.txt", "w") as a:
    a.write("Hello Cuties \n")
    a.write("Its Me Anay \n")
    a.write("Hehe \n")
    
with open("anay.txt" , "r") as a:
    content = a.read()
    
    print(content)
    
    
with open("anay.txt" , "r") as a:
    
    for l in a:
        print(l.strip())
        
#CSV are Comma Separated Values, to store tabular form data
with open("crops.csv", "w") as c:
     
    listies = {'Wheat': "10kg", "SugarCane":"20kg"}
    
    for item in listies:
        c.write(f"{item},{listies[item]}\n")