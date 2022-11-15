command_line = input()
product_dict = {}

while not command_line == 'buy':
    command_line = command_line.split()
    product, price, quantity = command_line[0], float(command_line[1]), int(command_line[2])
    if product not in product_dict:
        product_dict[product] = [price, quantity]
    else:
        product_dict[product][0] = price
        product_dict[product][1] += quantity
    command_line = input()
for name, value in product_dict.items():
    price = value[0]
    quantity = value[1]
    total_price = price * quantity
    print(f"{name} -> {total_price:.2f}")






