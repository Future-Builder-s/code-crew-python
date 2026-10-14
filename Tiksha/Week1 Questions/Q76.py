# Q76: Practice Question 76
# Create a before/after demonstration showing how `type()` can reveal an incorrect data type.

x = 5
print("\nBefore Conversion:", x, "\nType of x:", type(x))

x = str(x)
print("\nAfter Conversion:", x, "\nType of x:", type(x))