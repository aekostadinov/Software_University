count_of_nums = int(input())
bul = True

for _ in range(count_of_nums):
    num = int(input())
    if num % 2 == 1:
        print(f'{num} is odd!')
        bul = False
        break
    else:
        continue
if bul:
    print("All numbers are even.")