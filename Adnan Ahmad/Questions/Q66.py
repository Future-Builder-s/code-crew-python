# Q66. Create a conversion pipeline: string → integer → float → string. Print every intermediate value.

x = "50"
print(x, type(x))

x = int(x)
print(x, type(x))

x = float(x)
print(x, type(x))

x = str(x)
print(x, type(x))