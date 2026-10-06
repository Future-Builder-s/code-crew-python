#93Create a mini product-data transformation program using only variables, type(), and the covered type-conversion functions.
name = "Laptop"
price = "45999.50"
quantity = "10"
availability = True

price = float(price)
quantity = int(quantity)
availability = bool(availability)

print(name, type(name))
print(price, type(price))
print(quantity, type(quantity))
print(availability, type(availability))


#94Create a mini student-data transformation program where age, marks, and percentage begin in different representations and are converted into appropriate types.
name = "Priya"
age = "21"
marks = 90.5
percentage = "80.3"


age = int(age)
marks = int(marks)
percentage = float(percentage)


print(name, type(name))
print(age, type(age))
print(marks, type(marks))
print(percentage, type(percentage))

#95 Create a program that stores the same conceptual value in int, float, and str forms and clearly displays the difference.

a = 100
b = 100.0
c = "100"

print(a, type(a))
print(b, type(b))
print(c, type(c))

#96Create a program that demonstrates three correct conversions and one invalid conversion attempt. Keep the invalid attempt commented out and explain the expected issue in a code comment.
a = int("25")         #1: str to int
print(a, type(a))

b = float("3.14")      #2: str to float
print(b, type(b))

c = str(100)            # int to str
print(c, type(c))
# Invalid conversion attempt
# d = int("3.14")
# This causes a ValueError because "3.14" is not a valid integer string.

#97Create a compact 'Python Data Type Lab' program that creates examples of all covered basic types, prints each value, prints each type, and performs at least three conversions.
a = 10          #int
b = 3.14         #flt
c = "Python"     #string
d = True         #boolean

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d)) 

# Perform three conversions
a = float(a)     # int to float
b = int(b)       # float to int
c = str(a)       # float to string

# Print converted values and types
print(a, type(a))
print(b, type(b))
print(c, type(c))

#98Build a complete console-style data-type demonstration using only the concepts from this lecture: variables, assignment/reassignment, basic data types, type(), and type conversion. Include at least 10 variables and multiple conversion stages.
name = "Priya"
age = 21
price = 99.50
is_student = True
quantity = "5"
marks = "85"
weight = 50
distance = "12.5"
grade = "A"
status = 1

print(name, type(name))
print(age, type(age))
print(price, type(price))
print(is_student, type(is_student))
print(quantity, type(quantity))
print(marks, type(marks))
print(weight, type(weight))
print(distance, type(distance))
print(grade, type(grade))
print(status, type(status))

# Conversion Stage 1
quantity = int(quantity)
marks = int(marks)
distance = float(distance)

print(quantity, type(quantity))
print(marks, type(marks))
print(distance, type(distance))

# Conversion Stage 2
age = float(age)
price = int(price)
weight = str(weight)
print(age,type(age))
print(price,type(price))
print(weight,type(weight))

#conversion stage 3
quantity = str(quantity)
marks = float(marks)
status = bool(status)

print(quantity, type(quantity))
print(marks, type(marks))
print(status, type(status))


#99Build a type-audit program: create at least eight variables representing a realistic dataset, print each value with its type, then convert at least four values and print the updated values and types.
name = "Priya"
age = "18"
marks = "85.5"
roll_number = 101
attendance = "92"
fees = 15000
is_enrolled = True
grade = "A"

print(name, type(name))
print(age, type(age))
print(marks, type(marks))
print(roll_number, type(roll_number))
print(attendance, type(attendance))
print(fees, type(fees))
print(is_enrolled, type(is_enrolled))
print(grade, type(grade))


age = int(age)
marks = float(marks)
attendance = int(attendance)
is_enrolled = bool(is_enrolled)

print(age, type(age))
print(marks, type(marks))
print(attendance, type(attendance))
print(is_enrolled, type(is_enrolled))

#100. Create your own small real-world data record and write a program that demonstrates variable creation, reassignment, type inspection, and multiple valid type conversions without using any topic outside this lecture.
name = "Laptop"
price = "55000.50"
quantity = 10
weight = 2
available = True
year = 2026

print(name, type(name))
print(price, type(price))
print(quantity, type(quantity))
print(weight, type(weight))
print(available, type(available))
print(year, type(year))


price = float(price)       # str to float
quantity = float(quantity) # int to float
weight = str(weight)       # int to str
available = bool(available) # int to bool

print(price, type(price))
print(quantity, type(quantity))
print(weight, type(weight))
print(available, type(available))
