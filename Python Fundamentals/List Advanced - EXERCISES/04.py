numbers = [int(num) for num in input().split(", ")]
positive_numbers = [element for element in numbers if element >= 0]
negative_numbers = [element for element in numbers if element < 0]
even_numbers = [element for element in numbers if element % 2 == 0]
odd_numbers = [element for element in numbers if element % 2 != 0]

print("Positive: " + ", ".join(str(n) for n in positive_numbers))
print("Negative: " + ", ".join(str(n) for n in negative_numbers))
print("Even: " + ", ".join(str(n) for n in even_numbers))
print("Odd: " + ", ".join(str(n) for n in odd_numbers))
