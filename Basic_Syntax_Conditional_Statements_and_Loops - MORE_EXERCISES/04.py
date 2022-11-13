# user_input = str.lower(input())
# counter = 0
# index = 0
# beach_words = ["sand", "water", "fish", "sun"]
# for n in beach_words:
#     counter += user_input.count(n)
# print(counter)


user_input = input().lower()
count = (user_input.count('sand') + user_input.count('water') + user_input.count('fish') + user_input.count('sun'))
print(count)