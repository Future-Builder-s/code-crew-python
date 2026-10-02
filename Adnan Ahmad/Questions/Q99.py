# Q99. Build a type-audit program: create at least eight variables representing a realistic dataset, print each value with its type, then convert at least four values and print the updated values and types.

name = "Adnan Ahmad"
age = "20"
marks = "85"
percentage = "85.5"
height = 5.8
year = 2026
student_id = 1001
passed = True

print(name, type(name))
print(age, type(age))
print(marks, type(marks))
print(percentage, type(percentage))
print(height, type(height))
print(year, type(year))
print(student_id, type(student_id))
print(passed, type(passed))

age = int(age)
marks = int(marks)
percentage = float(percentage)
student_id = str(student_id)

print(age, type(age))
print(marks, type(marks))
print(percentage, type(percentage))
print(student_id, type(student_id))