# Create a small program with three conversion steps and verify every step with `type()`

x = "25"
print("Value of x:", x, "Type of x:", type(x))  

x = int(x)
print("Value of x:", x, "Type of x:", type(x))

x = float(x)
print("Value of x:", x, "Type of x:", type(x))