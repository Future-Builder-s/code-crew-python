# Create a shop item record, then convert the item's price from a string representation to float and verify the type

item_name = "Smartphone"
item_price = "499.99"  # Price as a string
item_price = float(item_price)  # Convert price to float

print("Item Name:", item_name, "Type:", type(item_name))
print("Item Price:", item_price, "Type:", type(item_price))