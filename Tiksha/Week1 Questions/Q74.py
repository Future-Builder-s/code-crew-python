# Q74: Practice Question 74
# Find and fix the type-conversion mistake in a short program you create yourself involving `int()` , `float()` , and `str()`

# Initial values with different types
age_str = "20"
height_str = "5.8"
weight_int = 65

# Correct conversions using int(), float(), and str()
age_int = int(age_str)              # String to Integer conversion
height_float = float(height_str)    # String to Float conversion
weight_str = str(weight_int)        # Integer to String conversion

# Display values and their types
print("\nAge (int):", age_int, type(age_int))
print("\nHeight (float):", height_float, type(height_float))
print("\nWeight (str):", weight_str, type(weight_str))
