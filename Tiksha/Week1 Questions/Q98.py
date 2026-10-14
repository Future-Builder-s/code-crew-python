# Q98: Practice Question 98
# Build a complete console-style data-type demonstration using only the concepts from this lecture: 
# variables, assignment/reassignment, basic data types, `type()`, and type conversion. 
# Include at least 10 variables and multiple conversion stages.

name = "Tiksha"
age = 20
cgpa = 9.25
active = True
score_str = "95"
price_str = "499.50"

print(name, type(name))
print(age, type(age))
print(cgpa, type(cgpa))
print(active, type(active))

# Next Year's age
age = 21
cgpa = float(int(cgpa))

score_int = int(score_str)
price_float = float(price_str)
price_int = int(price_float)
age_str = str(age)

print(score_int, type(score_int))
print(price_float, type(price_float))
print(price_int, type(price_int))
print(age_str, type(age_str))