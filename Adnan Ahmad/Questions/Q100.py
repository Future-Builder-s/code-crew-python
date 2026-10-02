# Q100. Create your own small real-world data record and write a program that demonstrates variable creation, reassignment, type inspection, and multiple valid type conversions without using any topic outside this lecture.

product_name = "Laptop"
price = "55000.50"
quantity = "2"
discount = 10.5
available = True
year = 2026

print(product_name, type(product_name))
print(price, type(price))
print(quantity, type(quantity))
print(discount, type(discount))
print(available, type(available))
print(year, type(year))

price = float(price)
print(price, type(price))

quantity = int(quantity)
print(quantity, type(quantity))

discount = str(discount)
print(discount, type(discount))

year = float(year)
print(year, type(year))

year = str(year)
print(year, type(year))