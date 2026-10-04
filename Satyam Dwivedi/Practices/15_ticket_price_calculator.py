# Movie Ticket Price Calculator
# Input for age and number of tickets
age = int(input("Enter your age: "))
num_of_tickets = int(input("Enter the number of tickets: "))
# ticket price slab
age_below_5 = num_of_tickets*50
age_5_to_17_or_60p = num_of_tickets*100
age_18_59 = num_of_tickets*150
# Condition 
if 0<= age < 5:
    print(f"Age: {age}")
    print(f"Tickets: {num_of_tickets}")
    print("Tecket Price: ₹50")
    print(f"Total Amount: ₹{age_below_5}")
elif 5 <= age <= 17:
    print(f"Age: {age}")
    print(f"Tickets: {num_of_tickets}")
    print("Tecket Price: ₹100")
    print(f"Total Amount: ₹{age_5_to_17_or_60p}") 
elif 18 <= age <= 59:
    print(f"Age: {age}")
    print(f"Tickets: {num_of_tickets}")
    print("Tecket Price: ₹150")
    print(f"Total Amount: ₹{age_18_59}") 
elif 60 <= age:
    print(f"Age: {age}")
    print(f"Tickets: {num_of_tickets}")
    print("Tecket Price: ₹100")
    print(f"Total Amount: ₹{age_5_to_17_or_60p}")
else:
    print("Error")
