# Q91. Build a type-conversion demonstration that starts with a numeric string and ends as a string again after passing through integer and float.

x = "100"
print(x, type(x))

x = int(x)
print(x, type(x))

x = float(x)
print(x, type(x))

x = str(x)
print(x, type(x))