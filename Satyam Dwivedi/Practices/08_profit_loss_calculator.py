# Profit, Loss Calculator
# Input for cost price
cp = float(input("Enter Cost Price: "))
# Input for Selling Price
sp = float(input("Enter Selling Price: "))

if sp > cp :
    print("Congratulations, you made a profit.")
    # Calculate Profit Amount
    p_a = sp - cp
    # print profit amount
    print(f"Profit Amount: {p_a}")
    # calculate profit percentage
    pp = (p_a*100)/cp
    #print profit percentage
    print(f"Percentage of Profit: {pp}%")
elif cp > sp:
    print("Sorry, you have incurred a loss.")
    # Calculate Loss Amount
    l_a =  cp - sp
    # print loss amount
    print(f"Loss Amount: {l_a}")
    # calculate loss percentage
    lp = (l_a*100)/cp
    # print loss percentage
    print(f"Loss Percentage: {lp}")
else :
    print("No Profit, No Loss")

