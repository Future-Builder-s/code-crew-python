#Q94. Create a mini student-data transformation program where age, marks, and percentage begin in different representations and are converted into appropriate types.

print("Student data transformation")
age = "20"
marks = "56"
percentage = 80
age_as_integer = int(age)
marks_as_integer = int(marks)
percentage_as_float = float(percentage)


print("Age:",age, "|Type:",type(age))
print("Marks:",marks, "|Type:",type(marks))
print("Percentage:",percentage, "|Type:",type(percentage))

print("="*50)
print("AFTER CHANGING TYPES")


print("Age:",age_as_integer, "|Type:",type(age_as_integer))
print("Marks:",marks_as_integer, "|Type:",type(marks_as_integer))
print("Percentage:",percentage_as_float, "|Type:",type(percentage_as_float))
