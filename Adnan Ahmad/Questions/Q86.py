# Q86. Create a shop item record, then convert the item's price from a string representation to float and verify the type.

item = "Laptop"
price = "55000.50"

print(price, type(price))

price = float(price)

print(price, type(price))