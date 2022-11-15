circle = input().split(' ')
kill_count = int(input())
result = []
counter = 0

index = 0
while len(circle) > 0:
    counter += 1

    if counter % kill_count == 0:
        result.append(circle.pop(index))
    else:
        index += 1

    if index >= len(circle):
        index = 0

print(str(result).replace(' ', '').replace('\'', ''))

1 2 3 4 5 6 7
3