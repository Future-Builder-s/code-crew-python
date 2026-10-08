# Create five variables, deliberately choose suitable initial types, then convert at least three of them to different types. Verify every conversion.

# Integer
age = 25
print("Age (Integer):", age, "Type:", type(age))

# Float
height = 5.6
print("Height (Float):", height, "Type:", type(height))

# String
name = "Katty"
print("Name (String):", name, "Type:", type(name))

# Boolean
is_student = True
print("Is Student (Boolean):", is_student, "Type:", type(is_student))

# Convert variables to different types
age_as_float = float(age)
print("Age as Float:", age_as_float, "Type:", type(age_as_float))

height_as_int = int(height)
print("Height as Integer:", height_as_int, "Type:", type(height_as_int))

name_as_list = list(name)
print("Name as List:", name_as_list, "Type:", type(name_as_list))