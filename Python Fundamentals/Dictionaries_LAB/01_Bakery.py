"""You will receive a single line containing some food (keys) and quantities
(values). They will be separated by a single space (the first element is the
key, the second – the value, and so on). Create a dictionary with all the keys
and values and print it on the console"""



lst_of_products = input().split()
dict_of_products = {}

for index in range(0,len(lst_of_products),2):
    product = lst_of_products[index]
    quantity = lst_of_products[index + 1]
    dict_of_products[product] = int(quantity)
print(dict_of_products)
