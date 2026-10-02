# Q75. Write a program that deliberately changes one variable from int to str, then verify that the change really happened.

x = 100
print(x, type(x))

x = str(x)
print(x, type(x))