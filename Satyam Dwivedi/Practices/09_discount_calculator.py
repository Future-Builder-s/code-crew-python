# Smart Discount Calculator
# Input for price
price = float(input("Enter Price of Product: "))
#If the price is above 5000, calculate a 20% discount
if price > 5000:
    print("Congratulations, you have received a '20%' discount.")
    # calculate 20% discount
    cd20 = (20*price)/100
    # calculate final payable amount
    fpa20 =price - cd20
    # print discount amount
    print(f"Discount amount: {cd20}")
    # print final payable amount
    print(f"Final Payabel Amount: {fpa20}")
elif price >= 2000 and price <= 5000:
    print("Congratulations, you have received a '10%' discount.")
    # calculate 10% discount
    cd10 = (10*price)/100
    # calculate final payable amount
    fpa10 =price - cd10
    # print discount amount
    print(f"Discount amount: {cd10}")
    # print final payable amount
    print(f"Final Payable Amount: {fpa10}")
else:
    print("Congratulations, you have received a '5%' discount.")
    # calculate 5% discount
    cd5 = (5*price)/100
    # calculate final payable amount
    fpa5 =price - cd5
    # print discount amount
    print(f"Discount amount: {cd5}")
    # print final payable amount
    print(f"Final Payabel Amount: {fpa5}")
