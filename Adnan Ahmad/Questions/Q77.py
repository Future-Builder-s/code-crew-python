# Q77. Create a small program with three conversion steps and verify every step with type().

x = "100"
print(type(x))

x = int(x)
print(type(x))

x = float(x)
print(type(x))

x = str(x)
print(type(x))