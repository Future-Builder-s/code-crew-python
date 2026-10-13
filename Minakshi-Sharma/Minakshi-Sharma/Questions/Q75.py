#Q75. Write a program that deliberately changes one variable from `int` to `str`, then verify that the change really happened.

a = 67
b = str(a)

print(b)
print(type(a))
print(type(b))
