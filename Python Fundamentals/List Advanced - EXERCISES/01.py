first_string = input().split(", ")
second_string = input().split(", ")
substring = [x for x in first_string if any(x in y for y in second_string)]
print(substring)



