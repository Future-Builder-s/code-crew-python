# Q97. Create a compact 'Python Data Type Lab' program that creates examples of all covered basic types, prints each value, prints each type, and performs at least three conversions.

integer_value = 25
float_value = 25.5
string_value = "100"
boolean_value = True

print(integer_value, type(integer_value))
print(float_value, type(float_value))
print(string_value, type(string_value))
print(boolean_value, type(boolean_value))

string_value = int(string_value)
print(string_value, type(string_value))

integer_value = float(integer_value)
print(integer_value, type(integer_value))

boolean_value = str(boolean_value)
print(boolean_value, type(boolean_value))