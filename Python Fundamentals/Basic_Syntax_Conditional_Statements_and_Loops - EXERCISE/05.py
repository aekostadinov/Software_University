number_of_orders = int(input())
total_price = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if not 1 <= days <= 31 or not 1 <= capsules_per_day <= 2000 or not 0.01 <= price_per_capsule <= 100:
        continue
    price_per_order = price_per_capsule * days * capsules_per_day
    total_price += price_per_order
    print(f"The price for the coffee is: ${price_per_order:.2f}")
print(f"Total: ${total_price:.2f}")

