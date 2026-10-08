#  Build a type-conversion demonstration that starts with a numeric string and ends as a string again after passing through integer and float.

numeric_string = "123"
print("Original (String):", numeric_string, "Type:", type(numeric_string))

numeric_int = int(numeric_string)
print("Converted (Integer):", numeric_int, "Type:", type(numeric_int))

numeric_float = float(numeric_int)
print("Converted (Float):", numeric_float, "Type:", type(numeric_float))

final_string = str(numeric_float)
print("Final (String):", final_string, "Type:", type(final_string))