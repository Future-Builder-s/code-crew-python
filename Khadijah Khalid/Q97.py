# Create a compact 'Python Data Type Lab' program that creates examples of all covered basic types, prints each value, prints each type, and performs at least three conversions.

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

# Conversions
age_as_float = float(age)
print("Age as Float:", age_as_float, "Type:", type(age_as_float))

height_as_int = int(height)
print("Height as Integer:", height_as_int, "Type:", type(height_as_int))

name_as_list = list(name)
print("Name as List:", name_as_list, "Type:", type(name_as_list))