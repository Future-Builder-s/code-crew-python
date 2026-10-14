# Q77: Practice Question 77
# Create a small program with three conversion steps and verify every step with `type()`.

x = 5
print("\nBefore Conversion:", x, "\nType of x:", type(x))

x = str(x)
print("\nAfter Conversion from int to str:", x, "\nType of x:", type(x))

x = float(x)
print("\nAfter Conversion from str to float:", x, "\nType of x:", type(x))