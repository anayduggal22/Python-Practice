
def Source_To_Middle(curr):

    if curr == 'USD':
        return 1
    elif curr == 'EUR':
        return 1.17
    elif curr == 'CAD':
        return 0.73
    else:
        return 0
    
def Middle_To_Target(curr):

    if curr == 'USD':
        return 1
    elif curr == 'EUR':
        return 0.85
    elif curr == 'CAD':
        return 1.37
    else:
        return 0
    

old_money = int(input("Enter Amount: \t"))

s = input("Enter Source (USD/EUR/CAD): \t")

money = old_money*Source_To_Middle(s)

t = input("Enter Target (USD/EUR/CAD): \t")

money *= Middle_To_Target(t)

print(f"{old_money}.0 {s} is equal to {money}.00")