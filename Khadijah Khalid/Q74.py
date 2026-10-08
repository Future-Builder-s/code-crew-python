# Find and fix the type-conversion mistake in a short program you create yourself involving `int()`, `float()`, and 'str()'

age = "19"
height = 5.7

age = int(age)
height = int(height)
age = str(age)

print(age + str(height))  # Error: string + float