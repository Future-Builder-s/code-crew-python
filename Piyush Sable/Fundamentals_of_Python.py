
# Print your first line of code
print("Hello World, this Piyush")

# Python is a Case-sensetive language
# What are the variable
# Can not declare a variable with number, speacial character, puctuation, already defined key word except underscore (_)

NAME = "Piyush"
age = 20
is_employed = False
height = 5.8
print(NAME)
print(age)
print(height)
print(is_employed)

# Data types
print(type(NAME))
print(type(age))
print(type(height))
print(type(is_employed))

# Input Function & f-string

name = input("Enter your name: ")
print(f"Hi {name}, Welcome the Python Fundamental session.")

#   Arithmatic Operators

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
print(f"The sum of {a} and {b} is {a+b}")
print(f"The Difference of {a} and {b} is {a-b}")
print(f"The Division of {a} and {b} is {a/b}")
print(f"The Product of {a} and {b} is {a*b}")

# Comparison Operators

a=10
b=12
print(a>b)
print(a<b)
print(a>=b)
print(a==b)
print(a!=b)
print("The Sum of a and b is: ", a+b)

"""# Decision making"""
# if-elif-alse

num=int(input("enter a number: "))
if num % 2==0:
 print(f"The {num} is even")
else:
  print("The number is odd")

num=int(input("enter a number: "))
if num>0:
 print(f"The {num} is positive")
elif num<0:
  print(f"The {num} is negative")
else:
    print(f"The {num} is neutral")

"""# If student is getting >90 "Excellent", >80 "very Good", >70 "Good", >60 "Fair", <40 "Fail"
"""

num=int(input("enter a number: "))
if num>90:
 print(f"The {num} is Excellent Mark")
elif num>80:
  print(f"The {num} is very Good Mark")
elif num>70:
 print(f" The {num} is Good Mark")
elif num>60:
  print(f" The {num} is Fair Mark")
elif num>40:
    print(f" The {num} is Pass Mark")
else:
    print(f" The {num} is Fail Mark")

# Loop for and While

for i in range(4,10):
  print(i)

# Print all the even number from 1 to 10

for i in range(1, 11):
  if i % 2==0:
    print(i)

# Do for revers order

for i in range(20, 0, -2):
  print(i)

for i in range(100):
 if i % 7==0 and i % 3==0:
  print(i)

# Print square of all the even number from 1 to 10

for i in range(11):
  if i % 2==0:
    print(i**2)


for i in range(1, 11):
  if i%2==0:
    print(i, "=", i**2)

# Create list of fruits

fruits= ['apple','orange','pineapple','watermelonn']

for fruit in fruits:
  print(fruits)


fruits= ['aPple','oraNge','pinEapple','wAtermElon']

for fruit in fruits:
  print(fruit.lower())

# check for palindrome in the given list
names = ['priya','Meenakshi','pooja','aatish','divya','naman','dad']

for name in names:
  if name == name[::-1]:
    print(f"The {name} is palindrome.")

#  While loop
lucky_no = 777
while True:
 guess_no = int(input('Enter your guess number'))
 if guess_no > 99:
  if guess_no == lucky_no:
     print("congratulation, you hav won a price.")
     break
 else:
   print("Try next time....")
else:
  print("Please entre any 3- digit number.")
