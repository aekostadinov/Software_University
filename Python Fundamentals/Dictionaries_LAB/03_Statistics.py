"""You will be receiving key-value pairs on separate lines
separated by ": " until you receive the command "statistics".
Sometimes you may receive a product more than once.
In that case, you have to add the new quantity to the existing one.
When you receive the "statistics" command, print the following:

"Products in stock:

- {product1}: {quantity1}

- {product2}: {quantity2}

…

- {productN}: {quantityN}

Total Products: {count_all_products}

Total Quantity: {sum_all_quantities}""""




command_line = input()
dict_product = {}

while not command_line == "statistics":
    command = command_line.split(": ")
    product = command[0]
    quantity = command[1]
    if product not in dict_product:
        dict_product[product] = 0
    dict_product[product] += int(quantity)
    command_line = input()

print("Products in stock:")
for key, value in dict_product.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(dict_product)}")
print(f"Total Quantity: {sum(dict_product.values())}")
