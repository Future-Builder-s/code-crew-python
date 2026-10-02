# Q94. Create a mini student-data transformation program where age, marks, and percentage begin in different representations and are converted into appropriate types.

name = "Adnan Ahmad"
age = "20"
marks = 85.0
percentage = "85.5"

age = int(age)
marks = int(marks)
percentage = float(percentage)

print(name, type(name))
print(age, type(age))
print(marks, type(marks))
print(percentage, type(percentage))