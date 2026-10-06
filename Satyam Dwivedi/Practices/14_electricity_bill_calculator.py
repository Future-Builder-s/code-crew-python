# Electricity Bill Calculator
# Input consumed units
units = float(input("Enter consumed units: "))
# Slab
# If 0–100 units have been consumed, a rate of 5 will apply
slab5rs = units*5
# If 101–200 units have been consumed, a rate of 7 will apply
slab7rs = units*7
# If 201–300 units have been consumed, a rate of 10 will apply
slab10rs = units*10
# If 300+ units have been consumed, a rate of 15 will apply
slab15rs = units*15

# Condition 

if 0 <= units <= 100:
    print(f"Units consumed: {units}")
    print("Rate: ₹5/unit")
    print(f"Your electricity bill amount: {slab5rs}")
elif 101 <= units <= 200:
    print(f"Units consumed: {units}")
    print("Rate: ₹7/unit")
    print(f"Your electricity bill amount: {slab7rs}")
elif 201 <= units <= 300:
    print(f"Units consumed: {units}")
    print("Rate: ₹10/unit")
    print(f"Your electricity bill amount: {slab10rs}")
elif 301 <= units :
    print(f"Units consumed: {units}")
    print("Rate: ₹15/unit")
    print(f"Your electricity bill amount: {slab15rs}")