# Q75: Practice Question 75
# Write a program that deliberately changes one variable from `int` to `str` , then verify that the change really happened.

x = 10
print("\nBefore Conversion from int to str:", x, "\nType of x:", type(x))

x = str(x)
print("\nAfter Conversion from int to str:", x, "\nType of x:", type(x))