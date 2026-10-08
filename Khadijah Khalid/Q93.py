#  Create a mini product-data transformation program using only variables, `type()`, and the covered type-conversion functions.

product_name = "Smartphone"
product_price_str = "499.99"  # Price as a string
product_price = float(product_price_str)  # Convert to float
product_quantity = 10  # Quantity as an integer
product_total = product_price * product_quantity  # Calculate total

print("Product Name:", product_name, "Type:", type(product_name))
print("Product Price (Float):", product_price, "Type:", type(product_price))
print("Product Quantity (Integer):", product_quantity, "Type:", type(product_quantity))
print("Product Total (Float):", product_total, "Type:", type(product_total))