#Q98. Build a complete console-style data-type demonstration using only the concepts from this lecture: variables, assignment/reassignment, basic data types, `type()`, and type conversion. Include at least 10 variables and multiple conversion stages.



# Initializing 10 variables with various basic data types
v1 = "500"      # str
v2 = "45.50"    # str
v3 = 100        # int
v4 = 9.81       # float
v5 = True       # bool
v6 = "Python"   # str
v7 = 25         # int
v8 = 3.14       # float
v9 = False      # bool
v10 = "2026"    # str

print("=== 1. INITIAL VARIABLES AND TYPES ===")
print("v1:", v1, "| Type:", type(v1))
print("v2:", v2, "| Type:", type(v2))
print("v3:", v3, "| Type:", type(v3))
print("v4:", v4, "| Type:", type(v4))
print("v5:", v5, "| Type:", type(v5))
print("v6:", v6, "| Type:", type(v6))
print("v7:", v7, "| Type:", type(v7))
print("v8:", v8, "| Type:", type(v8))
print("v9:", v9, "| Type:", type(v9))
print("v10:", v10, "| Type:", type(v10))

# Reassignment demonstration
print("\n=== 2. REASSIGNMENT STAGE ===")
v3 = "One Hundred"  
v4 = 50             
print("v3 after reassignment:", v3, "| Type:", type(v3))
print("v4 after reassignment:", v4, "| Type:", type(v4))

# Type Conversions 
print("\n=== 3. TYPE CONVERSION STAGE ===")
conv1 = int(v1)      
conv2 = float(v2)    
conv3 = str(v7)     
conv4 = int(v5)      

print("conv1 (str to int):", conv1, "| Type:", type(conv1))
print("conv2 (str to float):", conv2, "| Type:", type(conv2))
print("conv3 (int to str):", conv3, "| Type:", type(conv3))
print("conv4 (bool to int):", conv4, "| Type:", type(conv4))

