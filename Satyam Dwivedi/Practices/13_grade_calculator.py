# Grade Calculator
#  input marks
marks = int(input("Enter your marks (0-100): "))
# Determine grade
if marks < 0 or marks > 100:
    # print invalid marks enter
    print(f"{marks} is invalid marks.")
elif 90 <= marks <= 100:
    print("You got 'A Grade'") 
elif 80 <= marks <= 89:
    print("You got 'B Grade'") 
elif 70 <= marks <= 79:
    print("You got 'C Grade'") 
elif 60 <= marks <= 69:
    print("You got 'D Grade'") 
elif 50 <= marks <= 59:
    print("You got 'E Grade'") 
elif 0 <= marks < 50:
    print("You got 'F Grade'")