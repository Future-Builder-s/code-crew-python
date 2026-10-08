#  Build a type-audit program: create at least eight variables representing a realistic dataset, print each value with its type, then convert at least four values and print the updated values and types.

# Variables representing a realistic dataset
name = "Katty"  
age = 25
height = 5.6
is_student = True
grades = [85, 90, 78, 92]
coordinates = (10, 20)
person = {"name": "Alice", "age": 30}
unique_numbers = {1, 2, 3, 4, 5}

# Print each value with its type
print(name, "Type:", type(name))
print(age, "Type:", type(age))
print(height, "Type:", type(height))
print(is_student, "Type:", type(is_student))
print(grades, "Type:", type(grades))
print(coordinates, "Type:", type(coordinates))
print(person, "Type:", type(person))
print(unique_numbers, "Type:", type(unique_numbers))

# Convert at least four values and print the updated values and types
name_as_list = list(name)
print(name_as_list, "Type:", type(name_as_list))

age_as_float = float(age)
print(age_as_float, "Type:", type(age_as_float))

height_as_int = int(height)
print(height_as_int, "Type:", type(height_as_int))

is_student_as_int = int(is_student)
print(is_student_as_int, "Type:", type(is_student_as_int))