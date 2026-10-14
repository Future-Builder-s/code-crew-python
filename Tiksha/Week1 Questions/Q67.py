# Q67: Practice Question 67
# Create a conversion pipeline: integer → string → integer → float. Print the type after every conversion.

x = 86
print("\nBefore conversion:", x, "\nType of x:", type(x))

x = str(x)
print("\nFirst conversion:", x, "\nType of x:", type(x))

x = int(x)
print("\nSecond conversion:", x, "\nType of x:", type(x))

x = float(x)
print("\nThird conversion:", x, "\nType of x:", type(x))