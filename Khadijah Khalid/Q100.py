# Create your own small real-world data record and write a program that demonstrates variable creation, reassignment, type inspection, and multiple valid type conversions without using any topic outside this lecture.

# Student Data Record

name = "Khadijah"
age = 19
marks = 85
percentage = 85.5
student_id = "2026"

# Check original types
print(name, type(name))
print(age, type(age))
print(marks, type(marks))
print(percentage, type(percentage))
print(student_id, type(student_id))

# Reassignment and type conversion

# Age: integer -> float -> string
age = float(age)
print(age, type(age))

age = str(age)
print(age, type(age))

# Marks: integer -> string -> integer
marks = str(marks)
print(marks, type(marks))

marks = int(marks)
print(marks, type(marks))

# Percentage: float -> integer -> string
percentage = int(percentage)
print(percentage, type(percentage))

percentage = str(percentage)
print(percentage, type(percentage))

# Student ID: string -> integer -> float
student_id = int(student_id)
print(student_id, type(student_id))

student_id = float(student_id)
print(student_id, type(student_id))