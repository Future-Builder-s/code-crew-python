# Q86: Practice Question 86
# Create a shop item record, then convert the item's price from a string representation to float and verify the type.

item_name = "Laptop"                 # str
item_price_str = "99999.99"          # str

# Convert item_price_str to float
item_price_float = float(item_price_str)  # float

print("\nItem Name:", item_name, "\nType of item_name:", type(item_name))
print("\nItem Price (String):", item_price_str, "\nType of item_price_str:", type(item_price_str))
print("\nItem Price (Float):", item_price_float, "\nType of item_price_float:", type(item_price_float))