# Q93. Create a mini product-data transformation program using only variables, type(), and the covered type-conversion functions.

name = "Laptop"
price = "55000.50"
quantity = "5"
available = True

print(name, type(name))
print(price, type(price))
print(quantity, type(quantity))
print(available, type(available))

price = float(price)
quantity = int(quantity)
available = str(available)

print(price, type(price))
print(quantity, type(quantity))
print(available, type(available))