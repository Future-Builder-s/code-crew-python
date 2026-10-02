# Q88. Create a product price as a string, convert it to float, convert that float to integer, and show the type after each step.

price = "999.99"
print(price, type(price))

price = float(price)
print(price, type(price))

price = int(price)
print(price, type(price))