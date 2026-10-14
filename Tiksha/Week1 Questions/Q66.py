# Q66: Practice Question 66
# Create a conversion pipeline: string → integer → float → string. Print every intermediate value.

x = "66"
print("\nBefore conversion:", x, "\nType of x:", type(x))

x = int(x)
print("\nFirst conversion:", x, "\nType of x:", type(x))

x = float(x)
print("\nSecond conversion:", x, "\nType of x:", type(x))

x = str(x)
print("\nThird conversion:", x, "\nType of x:", type(x))