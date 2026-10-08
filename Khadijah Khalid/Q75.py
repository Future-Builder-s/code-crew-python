#  Write a program that deliberately changes one variable from `int` to `str`, then verify that the change really happened.

value = 10
print(type(value))  # <class 'int'>

value = str(value)
print(type(value))  # <class 'str'> 