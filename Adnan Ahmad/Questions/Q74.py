# Q74. Find and fix the type-conversion mistake in a short program you create yourself involving int(), float(), and str().

num = "25.5"

num = float(num)
num = int(num)
num = str(num)

print(num)
print(type(num))