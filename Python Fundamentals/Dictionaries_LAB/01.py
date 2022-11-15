lst_of_products = input().split()
dict_of_products = {}

for index in range(0,len(lst_of_products),2):
    product = lst_of_products[index]
    quantity = lst_of_products[index + 1]
    dict_of_products[product] = int(quantity)
print(dict_of_products)