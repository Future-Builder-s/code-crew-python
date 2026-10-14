#Q96. Create a program that demonstrates three correct conversions and one invalid conversion attempt. Keep the invalid attempt commented out and explain the expected issue in a code comment

a = "Minakshi Sharma"
b = "67"
c = 48
d = 678.8

print(a,type(a))
print(b,type(b))
print(c,type(c))

print("=" * 50)
print("CONVERTING TO SUITABLE TYPE")

# a = int(a) -> Invalid because a text string cannot be converted to an integer. 
b = int(b)
c = str(c)
d = int(d)

print(b,type(b))
print(c,type(c))
print(d,type(d))
