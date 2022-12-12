"""Write a program that reads students' names and their grades and adds them to the student record.
On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a
student's name and their grade. For each student print all his/her grades and finally his/her average grade, formatted
to the second decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
The order in which we print the result does not matter"""


num_of_lines = int(input())
information = {}

for _ in range(num_of_lines):
    line = tuple(input().split())
    name, grade = line
    if name not in information:
        information[name] = []
    information[name].append(float(grade))
for name, grade in information.items():
    formating_grade = [f"{el:.2f}" for el in grade]
    print(f"{name} -> {' '.join(str(num) for num in formating_grade)} (avg: {sum(grade)/len(grade):.2f})")



