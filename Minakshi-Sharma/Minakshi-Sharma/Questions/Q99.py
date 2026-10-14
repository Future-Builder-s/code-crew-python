#Q99. Build a type-audit program: create at least eight variables representing a realistic dataset, print each value with its type, then convert at least four values and print the updated values and types.

print("Type audit program")

product_name = "Sugar"
price_per_kg = 76
quantity = 20
total_amount = price_per_kg * quantity
is_available = True
discount_percent = 5.5
customer_name = "Rahul"
store_id = "ST102"

print(product_name, type(product_name))
print(price_per_kg, type(price_per_kg))
print(quantity, type(quantity))
print(total_amount, type(total_amount))
print(is_available, type(is_available))
print(discount_percent, type(discount_percent))
print(customer_name, type(customer_name))
print(store_id, type(store_id))

print("-" * 30)

price_per_kg = float(price_per_kg)
quantity = str(quantity)
total_amount = str(total_amount)
is_available = int(is_available)

print(price_per_kg, type(price_per_kg))
print(quantity, type(quantity))
print(total_amount, type(total_amount))
print(is_available, type(is_available))

