# Q96. Create a program that demonstrates three correct conversions and one invalid conversion attempt. Keep the invalid attempt commented out and explain the expected issue in a code comment.

x = "100"
x = int(x)
print(x, type(x))

x = float(x)
print(x, type(x))

x = str(x)
print(x, type(x))

# invalid = int("25.5")
# This would raise a ValueError because "25.5" is not a valid integer string.