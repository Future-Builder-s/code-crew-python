## Q92. Create five variables, deliberately choose suitable initial types, then convert at least three of them to different types. Verify every conversion.


product_name = "Notebook"       
quantity = 5                    
price_per_unit = 45.50          
is_in_stock = True              
discount_code = "DISCOUNT10"    

print("--- Initial Values and Types ---")
print("Product Name:", product_name, "| Type:", type(product_name))
print("Quantity:", quantity, "| Type:", type(quantity))
print("Price per Unit:", price_per_unit, "| Type:", type(price_per_unit))
print("In Stock:", is_in_stock, "| Type:", type(is_in_stock))
print("Discount Code:", discount_code, "| Type:", type(discount_code))

print("\n" + "="*40 + "\n")


print("--- After Type Conversions ---")


quantity_float = float(quantity)
print("Converted Quantity to float:", quantity_float, "| New Type:", type(quantity_float))


stock_int = int(is_in_stock)
print("Converted In Stock to int:", stock_int, "| New Type:", type(stock_int))


price_int = int(price_per_unit)
print("Converted Price to int:", price_int, "| New Type:", type(price_int))
