count_of_nums = int(input())
positive_nums = []
negative_nums = []

for _ in range(count_of_nums):
    num = int(input())
    if num >= 0:
        positive_nums.append(num)
    else:
        negative_nums.append(num)

print(f"{positive_nums}\n{negative_nums}")
print(f"Count of positives: {len(positive_nums)}")
print(f"Sum of negatives: {sum(negative_nums)}")

