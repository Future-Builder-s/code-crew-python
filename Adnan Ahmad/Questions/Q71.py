# Q71. A program converts `"3.14"` directly to `int`. Rewrite it so the value is first represented correctly as a float.

num = "3.14"

# original program 
'''
num = int(num)
'''

# modified version
num = float(num)
print(num, type(num))