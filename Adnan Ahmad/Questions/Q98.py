# Q98. Build a complete console-style data-type demonstration using only the concepts from this lecture: variables, assignment/reassignment, basic data types, type(), and type conversion. Include at least 10 variables and multiple conversion stages.

name = "Adnan Ahmad"
age = "20"
marks = 85
percentage = "85.5"
grade = "A"
passed = True
height = 5.8
year = 2026
score = "100"
active = True

print(name, type(name))
print(age, type(age))
print(marks, type(marks))
print(percentage, type(percentage))
print(grade, type(grade))
print(passed, type(passed))
print(height, type(height))
print(year, type(year))
print(score, type(score))
print(active, type(active))

age = int(age)
print(age, type(age))

percentage = float(percentage)
print(percentage, type(percentage))

score = int(score)
print(score, type(score))

score = float(score)
print(score, type(score))

score = str(score)
print(score, type(score))