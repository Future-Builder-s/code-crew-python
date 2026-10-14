# Q71: Practice Question 71
# A program converts `"3.14"` directly to `int` . Rewrite it so the value is first represented correctly as a float.

x = "3.14"
x = float(x)
print("\nAfter Fixing:", x, "\nType of x:", type(x))

x = int(x)
print("\nAfter Conversion from float to int:", x, "\nType of x:", type(x))