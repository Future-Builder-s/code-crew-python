# Leap year checker
# Input from User
year = int(input("Enter a year: "))
# Check Condition for Leap year
condition1st = year%400
condition2st = year%100
condition3st = year%4
# Verify 
if condition1st == 0:
    # print a leap year
    print(f"{year} is a leap year.")
elif condition2st == 0:
    # print not a leap year
    print(f"{year} is not a leat year.")
elif condition3st == 0:
    # print a leap year
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leat year.")