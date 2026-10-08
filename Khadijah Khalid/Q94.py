# Create a mini student-data transformation program where age, marks, and percentage begin in different representations and are converted into appropriate types.

age_str = "18"  # Age as a string
marks_int = 95  # Marks as an integer
percentage_float = 85.5  # Percentage as a float

# Convert variables to appropriate types
age_int = int(age_str)
print("Age (Integer):", age_int, "Type:", type(age_int))

marks_float = float(marks_int)
print("Marks (Float):", marks_float, "Type:", type(marks_float))

percentage_str = str(percentage_float)
print("Percentage (String):", percentage_str, "Type:", type(percentage_str))