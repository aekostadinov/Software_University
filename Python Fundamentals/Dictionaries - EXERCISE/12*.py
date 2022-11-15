command_line = input()
submission_dict = {}
students_points = {}
bul = False
banned_name = ''

while not command_line == 'exam finished':
    command_line = command_line.split("-")
    if len(command_line) > 2:
        username = command_line[0]
        language = command_line[1]
        points = int(command_line[2])
        if language not in submission_dict:
            submission_dict[language] = 0
        submission_dict[language] += 1
        if username not in students_points:
            students_points[username] = []
        students_points[username].append(points)
    elif command_line[1] == 'banned':
        banned_name = command_line[0]
        bul = True
    command_line = input()

for name, points in students_points.items():
    students_points[name] = max(points)
if bul:
    students_points.pop(banned_name)
print('Results:')
for key,value in students_points.items():
    print(f"{key} | {value}")
print("Submissions:")
for key,value in submission_dict.items():
    print(f"{key} - {value}")



