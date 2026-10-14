# Q99: Practice Question 99
# Build a type-audit program: create at least eight variables representing a realistic dataset, print each value with
# its type, then convert at least four values and print the updated values and types.

name = "Kaira"
age = 22
height = 5.7
is_enrolled = True
marks = [98, 92, 95]
location = ("Haryana", "Panipat")
student_info = {"course": "BS", "year": 2026}
skills = {"Python", "SQL", "Java", "C"}

print(name, "Type:", type(name))
print(age, "Type:", type(age))
print(height, "Type:", type(height))
print(is_enrolled, "Type:", type(is_enrolled))
print(marks, "Type:", type(marks))
print(location, "Type:", type(location))
print(student_info, "Type:", type(student_info))
print(skills, "Type:", type(skills))

# conversions
name_list = list(name)
print("Converted Name to List:", name_list, "Type:", type(name_list))

age_float = float(age)
print("Converted Age to Float:", age_float, type(age_float))

height_int = int(height)
print("Converted Height to Int:", height_int, type(height_int))

enrolled_int = int(is_enrolled)
print("Converted Boolean to Int:", enrolled_int, type(enrolled_int))