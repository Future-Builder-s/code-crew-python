#Q67. Create a conversion pipeline: integer → string → integer → float. Print the type after every conversion

a = 45
b = str(a)
c = int(b)
d = float(c)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
