# Q96: Practice Question 96
# Create a program that demonstrates three correct conversions and one invalid conversion attempt. 
# Keep the invalid attempt commented out and explain the expected issue in a code comment.

# Correct Conversion 1: String to Integer
age_str = "25"
age_int = int(age_str)
print("Converted String to Int:", age_int, type(age_int))

# Correct Conversion 2: Integer to Float
marks_int = 85
marks_float = float(marks_int)
print("Converted Int to Float:", marks_float, type(marks_float))

# Correct Conversion 3: Float to String
price_float = 99.99
price_str = str(price_float)
print("Converted Float to String:", price_str, type(price_str))


#Invalid Conversion Attempt

# Invalid Conversion Attempt: Trying to convert non-numeric letters into an integer
# invalid_conversion = int("hello") 

# EXPLANATION: 
# The code above is commented out because Python cannot convert alphabetic text 
# like "hello" into a number. If uncommented, it will crash and raise a ValueError: 
# invalid literal for int() with base 10: 'hello'.