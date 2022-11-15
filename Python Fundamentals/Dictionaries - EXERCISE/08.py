command_line = input()
course_info = {}

while not command_line == 'end':
    command_line = command_line.split(" : ")
    course = command_line[0]
    name = command_line[1]
    if course not in course_info:
        course_info[course] = []
    course_info[course].append(name)
    command_line = input()
for key in course_info.keys():
    print(f"{key}: {len(course_info[key])}")
    names = course_info[key]
    for index in range(len(names)):
        print(f"-- {names[index]}",end="\n")
