number_count_stars = int(input())

for multiply in range(1 , number_count_stars + 1):
    print('*' * multiply)
for mul in range(number_count_stars - 1, 0, -1):
    print('*' * mul)