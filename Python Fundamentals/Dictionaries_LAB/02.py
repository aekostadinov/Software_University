lst_of_products = input().split()
searched_products = input().split()
dict_of_products = {}

for index in range(0, len(lst_of_products), 2):
    product = lst_of_products[index]
    quantity = lst_of_products[index + 1]
    dict_of_products[product] = int(quantity)

for word in searched_products:
    if word in dict_of_products:
        quantity = dict_of_products[word]
        print(f"We have {quantity} of {word} left")
    else:
        print(f"Sorry, we don't have {word}")
