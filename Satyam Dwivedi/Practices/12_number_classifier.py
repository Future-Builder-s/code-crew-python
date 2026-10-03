# Number Classifier
# Input Number
number = int(input("Enter Number: "))
# Condition 
if number > 0:
    # print number is positive
    print(f"{number} is a positive number.")
    #Check Even or Odd
    if number%2 == 0:
        print(f"{number} is even number.")
    else:
        print(f"{number} is Odd number.")
elif number < 0:
    # print number is negative
    print(f"{number} is an negative number.")
    # Check Even or Odd
    if number%2 == 0:
        print(f"{number} is even number.")
    else:
        print(f"{number} is Odd number.")
else:
    print(f"{number} is zero.")
