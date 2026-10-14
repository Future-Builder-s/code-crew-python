# Q94: Practice Question 94
# Create a mini student-data transformation program where age, marks, and percentage begin in different representations and are converted into appropriate types.

# Initial student data
student_name = "Alex"
student_age = "22"  # Age as a string
student_marks = 92.4  # Marks as a float

# Convert student_age to integer
student_age_int = int(student_age)

# Convert student_marks to integer
student_marks_int = int(student_marks)

# Calculate percentage
total_marks = 100
percentage = (student_marks_int / total_marks) * 100

# Display student data and percentage
print("\nStudent Name:", student_name, "Type:", type(student_name))
print("Student Age (String):", student_age, "Type:", type(student_age))
print("Student Age (Integer):", student_age_int, "Type:", type(student_age_int))
print("Student Marks (Float):", student_marks, "Type:", type(student_marks))
print("Student Marks (Integer):", student_marks_int, "Type:", type(student_marks_int))
print("Percentage (Float):", percentage, "Type:", type(percentage))