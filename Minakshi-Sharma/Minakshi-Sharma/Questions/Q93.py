#Q93. Create a mini product-data transformation program using only variables, `type()`, and the covered type-conversion function

print("Product-data-transformation")
name = "Books"
quantity = 42
price_per_book = 100

total_amount = quantity*price_per_book
overall_cost = str(total_amount)

print("The overall cost of all books is:",overall_cost)
print("Type of overall_cost:", type(overall_cost))
