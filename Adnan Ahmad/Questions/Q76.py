# Q76. Create a before/after demonstration showing how type() can reveal an incorrect data type.

age = "20"
print("Before:", type(age))

age = int(age)
print("After:", type(age))