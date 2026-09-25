# print function

print("Hello World") 

# Data types - there are 4 datatypes in python
# String - str - enclosed in "" 
# Integer - int - integers
# float - float - decimal numbers
# Boolean values - bool - true or false
name = "Sara"
age = 23
price = 23.33

# To get the data type of something, we can use type()
print(type(name))
print(type(age))
print(type("Hows lifeeee"))

# Printing multiple lines of text using one print function
print("""
  p
  y
  t
  h
  o
  n
!!!!
        """)

# Storing multiple lines of text in a variable
var = """
hi
guys!
hows life
"""

print(var)
print(type(var))

variii = 3.9000009
print(type(variii))

boolean = True
print(type(boolean)) # bool

# Converting the data type 
a = "2"
b = 2

# conversion
print(int(a) + b)

# Input function along with type casting
# input("Simple thing ")
var_store = int(input("Simple thing"))
print(var_store + 2)

# In python the result of a input statement is always
# a String
# need to apply type casting to change the data type.

val = input("Enter some value ")
print(type(val), val) # "22" , "Value", "9.909"
# default will be string.

val = float(input("Enter some value "))
print(type(val), val)
# input value is now float - it has been type casted

# -------------------------

name = input("Enter name: ")
age = input("Enter age")
marks = input("Enter marks")

# :
print("Welcome", name)
print("age: ", age)
print("marks = ", marks)
