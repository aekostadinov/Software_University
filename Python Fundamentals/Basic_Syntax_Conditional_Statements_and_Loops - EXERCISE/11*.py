#  recipe
# Eggs - 1 pack
# Flour - 1kg
# Milk - 0.250l

budget = float(input())
price_for_kg_flour = float(input())
price_for_eggs = 0.75 * price_for_kg_flour
price_for_liter_of_milk = 1.25 * price_for_kg_flour
total_price_of_products = price_for_kg_flour + price_for_eggs + price_for_liter_of_milk / 4
number_of_breads = 0
collected_eggs = 0

while budget > total_price_of_products:
    number_of_breads += 1
    collected_eggs += 3
    if number_of_breads % 3 == 0:
        loses_eggs = number_of_breads - 2
        collected_eggs -= loses_eggs
    budget -= total_price_of_products
print(f"You made {number_of_breads} loaves of Easter bread! Now you have {collected_eggs} eggs and {budget:.2f}BGN left.")


