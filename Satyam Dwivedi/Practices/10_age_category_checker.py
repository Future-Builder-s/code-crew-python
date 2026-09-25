# Age Category Checker
# Input for age
age = int(input("Enter Age: "))
# program that takes a person's age and categorizes them
# Age below 5
if age < 5:
    # print age category
    print("You are a Toddler")
# Age 5 to 12
elif age >= 5 and age <= 12:
    # print age category
    print("You are a Child")
elif age >= 13 and age <= 17:
    # print age category
    print("You are a Teenager")
elif age >= 18 and age <= 59:
    # print age category
    print("You are an Adult")
else:
    # print age category
    print("You are a Senior Citizen")