"""On the first line, you will receive a string of numbers separated by space. On the second line,
you'll receive a target number. Your task is to find all pairs of numbers whose sum equals the target number.

For each found pair print "{number} + {number} = {target_number}".
Then, save only the unique pairs. Note: (1, 2) and (2, 1) are unique.
Also, you should keep track of how many iterations you've done.
At the end print all the iterations done in format: "Iterations done: {total_number_of_iterations}".
On the following lines, print the unique pairs in the format: "(first_number, second_number)".
The order in which we print the result does not matter."""



numbers = [int(num) for num in input().split()]
target_num = int(input())
itteration_num = 0
set_of_tupples = set()
for k in range(0,len(numbers)):
    first_number = numbers[k]
    for m in range(k + 1, len(numbers)):
        second_number = numbers[m]
        current_sum = first_number + second_number
        if current_sum == target_num:
            print(f"{first_number} + {second_number} = {target_num}")
            tuple = first_number,second_number
            set_of_tupples.add(tuple)
        itteration_num += 1
print(f"Iterations done: {itteration_num}")
for t in set_of_tupples:
    print(t)



