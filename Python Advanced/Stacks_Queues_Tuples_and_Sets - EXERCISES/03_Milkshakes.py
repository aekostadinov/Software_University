"""First, you will be given two sequences of integers representing chocolates and cups of milk.
You have to start from the last chocolate and try to match it with the first cup of milk. If their values are equal, 
you should make a milkshake and remove both ingredients. Otherwise, you should move the cup of milk at the end of the 
sequence and decrease the value of the chocolate by 5 without moving it from its position.If any of the values are 
equal to or below 0, you should remove them from the records right before mixing them with the other ingredient.
When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left, you need 
to stop making chocolate milkshakes.

Input
    -On the first line of input, you will receive the integers representing the chocolate, separated by  ", ". 
    -On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
    
Output
    -On the first line, print:
        oIf you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
        oOtherwise: "Not enough milkshakes."
    -On the second line - print:
        oIf there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
        oOtherwise: "Chocolate: empty"
    -On the third line - print:
        oIf there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
        oOtherwise: "Milk: empty"""
def check_values():
    while cups_of_milk and cups_of_milk[0]<= 0:
        cups_of_milk.popleft()
    while chocolates and chocolates[-1] <= 0:
        chocolates.pop()
    if cups_of_milk and chocolates:
        return True


from collections import deque
chocolates = [int(num) for num in input().split(", ")]   # last
cups_of_milk = deque([int(num) for num in input().split(", ")]) # first
count_of_milkshakes = 0
while chocolates and cups_of_milk:
    if check_values():
        if chocolates[-1] == cups_of_milk[0]:
            count_of_milkshakes += 1
            cups_of_milk.popleft()
            chocolates.pop()
        else:
            cups_of_milk.append(cups_of_milk.popleft())
            chocolates[-1] -= 5
        if count_of_milkshakes == 5:
            break
if count_of_milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(num) for num in chocolates)}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(str(num) for num in cups_of_milk)}")
else:
    print("Milk: empty")


