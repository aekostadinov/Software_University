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
