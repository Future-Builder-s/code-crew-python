#Q86. Create a shop item record, then convert the item's price from a string representation to float and verify the type.


shop_name = "Garg Sales"
product_name = "Maggie"
per_unit_price_str = "₹20"


per_unit_price_float = float(per_unit_price_str.replace("₹", ""))

print("Per unit price:", per_unit_price_float)
print("Verified Type:", type(per_unit_price_float))
