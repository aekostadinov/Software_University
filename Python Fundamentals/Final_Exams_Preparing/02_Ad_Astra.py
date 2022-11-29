"""On the first line of the input, you will be given a text string. You must extract the 
information about the food and calculate the total calories. First, you must extract the
food info. It will always follow the same pattern rules:

    -It will be surrounded by "|" or "#" (only one of the two) in the following pattern:
    #{item name}#{expiration date}#{calories}#   or 
    |{item name}|{expiration date}|{calories}|

    -The item name will contain only lowercase and uppercase letters and whitespace

    -The expiration date will always follow the pattern: "{day}/{month}/{year}", where the day,
    month, and year will be exactly two digits long

    -The calories will be an integer between 0-10000

Calculate the total calories of all food items and then determine how many days you can last 
with the food you have. Keep in mind that you need 2000kcal a day.

Input / Constraints
  You will receive a single string
  
Output
  First, print the number of days you will be able to last with the food you have:
  "You have food to last you for: {days} days!"
  The output for each food item should look like this:
  "Item: {item name}, Best before: {expiration date}, Nutrition: {calories}"""




import re
pattern = re.compile(r'([\\|#])(?P<product>[A-Za-z ]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1')
products = input()
matches = pattern.finditer(products)
products = []
calories = 0
for match in matches:
    products.append(f"Item: {match['product']}, Best before: {match['date']}, Nutrition: {match['calories']}")
    calories += int(match['calories'])
calories_consumed_per_day = 2000
food_for_n_days = calories // calories_consumed_per_day
print(f"You have food to last you for: {food_for_n_days} days!")
[print(item) for item in products]