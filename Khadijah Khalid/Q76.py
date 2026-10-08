# Create a before/after demonstration showing how `type()` can reveal an incorrect data type.

x = "10"
print("Before conversion: Value of x:", x, "Type of x:", type(x))

x = int(x)
print("After conversion: Value of x:", x, "Type of x:", type(x))