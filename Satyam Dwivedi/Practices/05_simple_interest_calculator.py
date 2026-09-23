# Simple Interest Calculator
# Input for Principal amount
Prpl_amt = int(input("Enter Principal amount: "))
# Input for Rate of interest
r_f_i = int(input("Enter Rate of interest(in %): "))
# Input for Time in years
Time = int(input("Enter Time (in years): "))
# Calculat Simple Interest 
S_i = (Prpl_amt * r_f_i * Time)/ 100
# Print Simple interest
print(f"Simple Interest: {S_i}")
# Calculat Final Payable amount
fpa = Prpl_amt + S_i
# Print Final Payable Amount
print(f"Final Payable Amount: {fpa}")