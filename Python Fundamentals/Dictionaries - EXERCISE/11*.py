command_line = input()
force_user_information = {}


while not command_line == 'Lumpawaroo':
    if " | " in command_line:
        bul_force_user = True
        command_line = command_line.split(" | ")
        force_side = command_line[0]
        force_user = command_line[1]
        if force_side not in force_user_information:
            for value in force_user_information.values():
                if force_user in value:
                    bul_force_user = False
                    break
            if bul_force_user:
                force_user_information[force_side] = [force_user]
        elif force_side in force_user_information:
            for value in force_user_information.values():
                if force_user in value:
                    bul_force_user = False
                    break
            if bul_force_user:
                force_user_information[force_side].append(force_user)

    elif " -> " in command_line:
        bul_force_user = True
        command_line = command_line.split(" -> ")
        force_user = command_line[0]
        force_side = command_line[1]
        if force_side in force_user_information:
            for value in force_user_information.values():
                if force_user in value:
                    value.remove(force_user)
                    # index = value.index(force_user)
                    # force_user_information[force_side].append(value.pop(index))
                    # bul_force_user = False
                    # break
            if bul_force_user:
                force_user_information[force_side].append(force_user)
        elif force_side not in force_user_information:
            for value in force_user_information.values():
                if force_user in value:
                    value.remove(force_user)
                    # bul_force_user = False
                    # break
            if bul_force_user:
                force_user_information[force_side] = [force_user]
        print(f"{force_user} joins the {force_side} side!")
    command_line = input()
for side, user in force_user_information.items():
    if len(user) != 0:
        print(f"Side: {side}, Members: {len(user)}")
        for element in user:
            print(f"! {element}")











