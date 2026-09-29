##This is my first Python Program

print("My name is Priya.")
print("This is my First Python Program.")
print("Hello, World!")
print("My name is Priya","I am Learning Python Programming.")
print(55)
print(30+88)
print(70-45)
print(55/5)
print(30*9)


##Variables in Python

name = "Priya"
age = 21
price = 55.5
print("My name is:", name)
print("My age is:", age)
print("The price is:", price)



##data types in Python
name = "Priya" #string
age = 21 #integer
price = 55.5 #float
is_student = True #boolean  

age = 21
old = True
a = None
print(type(old))
print(type(a))

##Print sum
a = 1000
b = 2000
sum = a + b
print(sum)

##arithmetic operations
a = 5
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)# remainder
print(a ** b)#a^b

##relational operators
a = 50
b = 20
print(a == b)#False
print(a != b)#True
print(a > b)#True
print(a < b)#False
print(a >= b)#True
print(a <= b)#False


##assignment operators
num = 10
num += 10
print("num :", num)#20

##logical operators
a = 80
b = 50
print(not False)
print(not (a > b))

val1 = True
val2 = True
print("AND operator:", val1 and val2)#True
print("OR operator:", val1 or val2)#True
print("OR operator:", (a ==b or a > b))#True

##type conversion
a = 10
b = 20.5
sum = a + b#10.0 + 20.5 = 30.5
print(sum)

##type casting
a = int("5")
b = 4.25
print(type(a))
print(a + b)

##inputs in Python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Welcome", name, "Your age is", age, "and your marks are", marks)

##Practice Programs
#1Write a Program to input two numbers and print their sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The sum is=", a + b)

#2Write a Program to input side of a square and print its area
side = float(input("Enter the side of the square: "))
area = side * side
print("The area of the square is:", area)   

#3Write a Program to input 2 floating point numbers and print their average
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
average = (a + b) / 2
print("The average is:", average)

#4Write a Program to input 2 int numbers, a and b. Print True if a is greater than or equal to  b, otherwise print False
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a >= b)



