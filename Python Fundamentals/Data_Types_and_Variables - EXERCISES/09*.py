number_of_snowballs = int(input())
quality_of_snowball = 0
best_time = 0
best_weight = 0
best_quality = 0


for _ in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    result = (weight / time) ** quality
    if result > quality_of_snowball:
        quality_of_snowball = result
        best_time = time
        best_weight = weight
        best_quality = quality

print(f"{best_weight} : {best_time} = {int(quality_of_snowball)} ({best_quality})")



