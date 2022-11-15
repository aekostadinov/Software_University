command_line = input()
course_information = {}

while not command_line == 'End':
    command_line = command_line.split(" -> ")
    course = command_line[0]
    employee_id = command_line[1]
    if course not in course_information:
        course_information[course] = []
    if employee_id not in course_information[course]:
        course_information[course].append(employee_id)
    command_line = input()
for key, value in course_information.items():
    print(f"{key}")
    for index in range(len(value)):
        print(f"-- {value[index]}")
