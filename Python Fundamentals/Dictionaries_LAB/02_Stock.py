"""You will be given key-value pairs of products and quantities
(on a single line separated by space). On the following line, you
will be given products to search for. Check for each product.
You have 2 possibilities:

· If you have the product, print "We have {quantity} of {product} left".

· Otherwise, print "Sorry, we don't have {product}""""




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
