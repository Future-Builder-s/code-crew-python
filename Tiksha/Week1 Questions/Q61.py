# Q61: Practice Question 61
# Create a numeric string, convert it to float, then convert the float to string. Show each type.

x = "50"
print("\nBefore conversion:", x, "\nType of num:", type(x))

x = float(x)
print("\nFirst conversion:", x, "\nType of num:", type(x))

x = str(x)
print("\nSecond conversion:", x, "\nType of num:", type(x))
