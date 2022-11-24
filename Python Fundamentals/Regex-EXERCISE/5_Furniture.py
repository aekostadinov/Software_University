"""Write a program that calculates the total cost of bought furniture.
You will be given information about each purchase on separate lines until
you receive the command "Purchase". Valid information should be in the format:
">>{furniture_name}<<{price}!{quantity}". The price could be a floating-point
or integer number. You should store the names of the furniture and the total price.

In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:

"Bought furniture:
{1st name}
{2nd name}
…
{N name}
Total money spend: {total_cost}"""

import re
pattern =r">>(?P<Product>[A-Za-z]+)<<(?P<Price>\d+(\.\d+)?)!(?P<Quantity>\d+)\b"
furniture_names = []
total_sum = 0
line = input()

while not line == 'Purchase':
    match = re.match(pattern, line)
    if match:
        data = match.groupdict()
        furniture_names.append(data['Product'])
        total_sum += int(data['Quantity']) * float(data['Price'])
    line = input()
print("Bought furniture:")
if furniture_names:
    print("\n".join(furniture_names))
print(f"Total money spend: {total_sum:.2f}")
