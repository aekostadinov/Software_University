"""Write a program that finds the longest intersection. You will be given a number N. On each of the next N lines you
will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". You should find the
intersection of these two ranges. The start and end numbers in the ranges are inclusive.
Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its
length in the format: "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"

Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one."""


count_of_lines = int(input())
intersection_set = set()
for _ in range(count_of_lines):
    first_set_info, second_set_info = input().split("-")
    first_start, first_end = (int(x) for x in first_set_info.split(','))
    second_start, second_end = (int(y) for y in second_set_info.split(','))
    first_set = set(range(first_start,first_end+1))
    second_set = set(range(second_start, second_end+1))
    current_intersection = first_set.intersection(second_set)
    if len(current_intersection) > len(intersection_set):
        intersection_set = current_intersection
print(f"Longest intersection is {[number for number in intersection_set]} with length {len(intersection_set)}")



