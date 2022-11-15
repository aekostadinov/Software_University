train_ticket = 150
item_collection = input().split("|")
budget = float(input())
list_of_sell_products = []
profit = 0
sum_of_bought_products = 0

for index in range(len(item_collection)):
    to_buy = False
    list_of_separate_items = item_collection[index].split('->')
    type_of_clothes, price = list_of_separate_items[0], float(list_of_separate_items[1])
    if type_of_clothes == 'Clothes' and price <= 50:
        if budget >= price:
            to_buy = True
    elif type_of_clothes == 'Shoes' and price <= 35:
        if budget >= price:
            to_buy = True
    elif type_of_clothes == 'Accessories' and price <= 20.50:
        if budget >= price:
            to_buy = True
    if to_buy:
        budget -= price
        sum_of_bought_products += price
        list_of_sell_products.append(str(f"{price * 1.4:.2f}"))

print(" ".join(list_of_sell_products))
list_of_sell_products = list(map(float,list_of_sell_products))
profit = sum(list_of_sell_products) - sum_of_bought_products
print(f"Profit: {profit:.2f}")
if (budget + sum(list_of_sell_products)) >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")



