# Q91: Practice Question 91
# Build a type-conversion demonstration that starts with a numeric string and ends as a string again after passing through integer and float.

numeric_string = "123.45"
print("\nOriginal:", numeric_string, "Type:", type(numeric_string))

# Convert to float
float_var = float(numeric_string)
print("\nAfter float conversion:", float_var, "Type:", type(float_var))

# Convert to integer
int_var = int(float_var)
print("\nAfter integer conversion:", int_var, "Type:", type(int_var))

# Convert back to string
final_string = str(int_var)
print("\nFinal string:", final_string, "Type:", type(final_string))