"""Write a function called stock_availability which receives:
    -an inventory list of boxes with different kinds of cupcake flavours
    -"delivery" or "sell" as second parameter
    -there might or might not be any other parameters – numbers or strings at the end

In case of "delivery"  to the shop was delivered new boxes with diferent kinds of cupcakes:
    -You should add the boxes at the end of the inventory list
    -There will be always at least one box delivered
In case of "sell" Maria has a client and she is selling different boxes with cupcakes:
    -If there is a number as another parameter, it means that Maria has sold that many boxes with cupcakes and you
should remove them from the beginning of the inventory list
    -If there is/are string/s as another parameter/s, it means that Maria has sold ALL cupcake boxes of the ordered
flavour/s. Beware that not everything the buyer has ordered might be in stock, so you should check if the order is valid.
    -If there are no other parameters, it means that Maria has sold only the first box of cupcakes and you should remove
it of the inventory list
For more clarifications, see the examples below.

Input
    -There will be no input
    -Parameters will be passed to your function
Output
    -The function should return a new inventory list
    -All commands will be valid"""


def stock_availability(list_of_boxes, command, *args):
    if command == 'delivery':
        for cakes in args:
            list_of_boxes.append(cakes)
    elif command == 'sell':
        if args:
            for element in args:
                if str(element).isdigit():
                    if len(list_of_boxes) > element:
                        list_of_boxes = list_of_boxes[element:]
                    else:
                        list_of_boxes = []
                else:
                    while element in list_of_boxes:
                        list_of_boxes.remove(element)
        else:
            list_of_boxes.pop(0)
    return list_of_boxes



# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))