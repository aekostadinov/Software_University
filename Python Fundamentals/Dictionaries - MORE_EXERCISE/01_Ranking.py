command = input()
data_info = {}
contest_information = {}

while not command == 'end of contests':
    contest, pass_for_contest = command.split(":")
    data_info[contest] = pass_for_contest
    command = input()


command_line = input()
while not command_line == "end of submissions":
    contest, password, username, points = command_line.split("=>")
    points = int(points)
    if contest in data_info and data_info[contest] == password:
        if username not in contest_information:
            contest_information[username] = {contest: points}
        if contest in contest_information[username]:
            if contest_information[username][contest] > points:
                command_line = input()
                continue
            else:
                contest_information[username][contest] = points
        else:
            contest_information[username][contest] = points
    command_line = input()

total_points = 0
best_user = ''
for user, information in contest_information.items():
    current_points = 0
    for contest, points in information.items():
        current_points += information[contest]
    if current_points >= total_points:
        total_points = current_points
        best_user = user
print(f"Best candidate is {best_user} with total {total_points} points.")
print('Ranking:')
contest_information = dict(sorted(contest_information.items()))
for user,info in contest_information.items():
    contest_information[user] = dict(sorted(contest_information[user].items(),key=lambda x: x[1],reverse=True))
for name, info in contest_information.items():
    print(name)
    for contest,points in info.items():
        print(f"#  {contest} -> {points}")





