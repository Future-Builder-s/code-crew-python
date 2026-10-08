# Create a program that demonstrates three correct conversions and one invalid conversion attempt. Keep the invalid attempt commented out and explain the expected issue in a code comment.

# Valid Conversions
# String to Integer
age_str = "18"
age_int = int(age_str)

# Integer to Float
marks_int = 95
marks_float = float(marks_int)

# Float to String
percentage_float = 85.5
percentage_str = str(percentage_float)

# Invalid Conversion (commented out)
# invalid_conversion = int("not_a_number")  # This will raise a ValueError