# Q95: Practice Question 95
# Create a program that stores the same conceptual value in `int`,`float`, and `str` forms and clearly displays the difference.

value = 42
value_int = int(value)
value_float = float(value)
value_str = str(value)

print("\nValue as Integer:", value_int, "Type:", type(value_int))
print("Value as Float:", value_float, "Type:", type(value_float))
print("Value as String:", value_str, "Type:", type(value_str))
