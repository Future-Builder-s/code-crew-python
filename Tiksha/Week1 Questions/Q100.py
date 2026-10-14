# Q100: Practice Question 100
# Create your own small real-world data record and write a program that demonstrates variable creation,
# reassignment, type inspection, and multiple valid type conversions without using any topic outside this lecture.

# Real-world student record
student_name = "Tiara"
age = 22
marks = 92
percentage = 94.5
student_id = "2026"


print("--- Original Types ---")

print(student_name, type(student_name))
print(age, type(age))
print(marks, type(marks))
print(percentage, type(percentage))
print(student_id, type(student_id))


print("\n--- Conversions ---")

# Age: integer -> float -> string
age = float(age)
print("Age as float:", age, type(age))
age = str(age)
print("Age as string:", age, type(age))

# Marks: integer -> string -> integer
marks = str(marks)
print("Marks as string:", marks, type(marks))
marks = int(marks)
print("Marks back to int:", marks, type(marks))

# Percentage: float -> integer -> string
percentage = int(percentage)
print("Percentage as int:", percentage, type(percentage))
percentage = str(percentage)
print("Percentage as string:", percentage, type(percentage))

# Student ID: string -> integer -> float
student_id = int(student_id)
print("ID as int:", student_id, type(student_id))
student_id = float(student_id)
print("ID as float:", student_id, type(student_id))