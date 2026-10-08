# Create a conversion pipeline: string → integer → float → string. Print every intermediate value.

x = "25"
print("Value of x:", x)
x = int(x)
print("Value of x:", x)
x = float(x)
print("Value of x:", x)
x = str(x)
print("Value of x:", x)