# command_line = input().split(":")
# dict_course = {}
# dict_students = {}
#
# while len(command_line) == 3:
#     name = command_line[0]
#     name_id = int(command_line[1])
#     course = command_line[2].replace(" ", "_")
#
#     if course not in dict_course:
#         dict_course[course] = []
#     dict_course[course].append(name_id)
#     dict_students[name_id] = name
#
#     command_line = input().split(":")
# searched_course = " ".join(command_line)
# lst_of_id = dict_course[searched_course]
# for index in range(len(lst_of_id)):
#     id = lst_of_id[index]
#     student_name = dict_students[id]
#     print(f"{student_name} - {id}")
#




student = input()
students_dict = {}
while ":" in student:
    name, student_id, student_course = student.split(":")
    students_dict[name] = student_id, student_course

    student = input()

course = student.replace("_", " ")

for key, value in students_dict.items():
    student_id = value[0]
    student_course = value[1]
    if student_course == course:
        print(f'{key} - {student_id}')