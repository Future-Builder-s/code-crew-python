# Q93: Practice Question 93
# Create a mini product-data transformation program using only variables, `type()`, and the covered type-conversion functions.

# Initial product data
product_name = "Widget"
product_price = "19.99"  # Price as a string
product_quantity = 5  # Quantity as an integer

# Convert product_price to float for calculations
product_price_float = float(product_price)

# Calculate total cost
total_cost = product_price_float * product_quantity

# Convert total_cost to string for display
total_cost_str = str(total_cost)

# Display product data and total cost
print("\nProduct Name:", product_name, "Type:", type(product_name))
print("Product Price (String):", product_price, "Type:", type(product_price))
print("Product Price (Float):", product_price_float, "Type:", type(product_price_float))
print("Product Quantity:", product_quantity, "Type:", type(product_quantity))
print("Total Cost (Float):", total_cost, "Type:", type(total_cost))
print("Total Cost (String):", total_cost_str, "Type:", type(total_cost_str))