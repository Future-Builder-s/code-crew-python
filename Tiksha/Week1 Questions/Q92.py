# Q92: Practice Question 92
# Create five variables, deliberately choose suitable initial types, then convert at least three of them to different types. Verify every conversion.

var1 = 42  # Integer
var2 = 3.14  # Float
var3 = "Hello"  # String
var4 = True  # Boolean
var5 = [1, 2, 3]  # List

# Convert var1 to float
var1_float = float(var1)
print("\nvar1 (Integer) -> var1_float (Float):", var1_float, "Type:", type(var1_float))

# Convert var2 to integer
var2_int = int(var2)
print("var2 (Float) -> var2_int (Integer):", var2_int, "Type:", type(var2_int))

# Convert var4 to string
var4_str = str(var4)
print("var4 (Boolean) -> var4_str (String):", var4_str, "Type:", type(var4_str))
