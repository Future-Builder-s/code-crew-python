# Q92. Create five variables, deliberately choose suitable initial types, then convert at least three of them to different types. Verify every conversion.

age = 20
price = 99.5
marks = "85"
number = "100"
active = True

age = float(age)
price = str(price)
marks = int(marks)

print(age, type(age))
print(price, type(price))
print(marks, type(marks))
print(number, type(number))
print(active, type(active))