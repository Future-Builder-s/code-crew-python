#Q77. Create a small program with three conversion steps and verify every step with `type()`.

a = "55"
b = float(a)
c = int(b)
d = str(c)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
