count_of_pairs = int(input())
grades_information = {}


for _ in range(count_of_pairs):
    name = input()
    grade = float(input())
    if name not in grades_information:
        grades_information[name] = []
    grades_information[name].append(grade)

for name, grades in grades_information.items():
    average_grade = sum(grades)/len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")


