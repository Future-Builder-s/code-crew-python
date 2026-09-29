##This is my first python program
print("My name is Harsh.", "Nice to meet you!")
print("Hello, World!")
print(23)
print(23+5)


##variables in python
name="Harsh" 
age=20 #assignment operator
price=23.5 
age2=age
print("My name is", name, "and my age is", age2)


##Data types in python
# Integers- int
# Float- float
# String- str- enclosed in " "
# Boolean- bool- True/False
# None- NoneType

name="Harsh" #string
age=20 #integer
price=20.5 #float
old=False #boolean
a=None #null

print(type(name))
print(type(age))
print(type(price))
print(type(old))
print(type(a))


##Types of operators in python
#arithmetic operators 
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #remainder
print(a**b) #power
#relational operators
a= 50
b= 20
print(a==b)#False
print(a!=b)#True
print(a>b)#True
print(a<b)#False
print(a>=b)#True
print(a<=b)#False
#assignment operators
num1=10
num1+=10
num2=20
num2-=10
num3=30
num3*=10
num4=40
num4/=10 
num5=50
num5%=10
num6=6
num6**=3
print(num1)#20
print(num2)#10
print(num3)#300
print(num4)#4.0
print(num5)#0
print(num6)#216
#logical operators
a=50
b=30
print(not (a>b)) #False
print(not False) #True

val1=True
val2=True
val3=False
print("and operator:", val1 and val2) #True
print("and operator:", val1 and val3) #False
print("or operator:", val1 or val3) #True
print((a==b) or (a>b)) #True


##Type conversion in python
a=2
b=4.25

sum=a+b # 2.0 + 4.25 = 6.25
print(sum)


##Type casting in python
a=int("2")
b=4.25
sum=a+b # 2.0 + 4.25 = 6.25
print(sum)


##Inputs in python
name=input("Enter your name: ")
age=int(input("Enter your age: "))
marks=float(input("Enter your marks: "))

print("Welcome", name, "your age is", age, "and your marks are", marks)


##Practice problems
#1. Write a program to input 2 numbers & print their sum
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
sum=a+b
print("The sum is:", sum)
#2. WAP to input side of a square & print its area
a=float(input("Enter the side: "))
area=a**2
print("The area of the sq. is: " , area)
#3. WAP to input 2 floating point numbers & print their avg
a=float(input("Enter 1st: "))
b=float(input("Enter 2nd: "))
avg=(a+b)/2
print("The avg is: ", avg)
#4. WAP to input 2 int numbes,  and b. Print True if a is greater than or equal to b. If not print False.
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
print(a>=b)