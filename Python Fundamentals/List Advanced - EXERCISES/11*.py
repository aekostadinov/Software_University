schedule_of_lessons = input().split(", ")
command = input()

while not command == 'course start':
    command = command.split(":")
    if command[0] == "Add":
        lesson = command[1]
        if lesson not in schedule_of_lessons:
            schedule_of_lessons.append(lesson)
    elif command[0] == 'Insert':
        lesson_title = command[1]
        index = int(command[2])
        if lesson_title not in schedule_of_lessons:
            schedule_of_lessons.insert(index, lesson_title)
    elif command[0] == 'Remove':
        lesson_title = command[1]
        if lesson_title in schedule_of_lessons:
            schedule_of_lessons.remove(lesson_title)
            if (f"{lesson_title}-Exercise") in schedule_of_lessons:
                schedule_of_lessons.remove(f"{lesson_title}-Exercise")
    elif command[0] == 'Swap':
        first_lesson = command[1]
        second_lesson = command[2]
        if (first_lesson in schedule_of_lessons) and (second_lesson in schedule_of_lessons):
            index_1, index_2 = schedule_of_lessons.index(first_lesson), schedule_of_lessons.index(second_lesson)
            schedule_of_lessons[index_1], schedule_of_lessons[index_2] = schedule_of_lessons[index_2], schedule_of_lessons[index_1]
            if (f"{first_lesson}-Exercise") in schedule_of_lessons:
                i = schedule_of_lessons.index(f"{first_lesson}-Exercise")
                if index_1 == -1:
                    schedule_of_lessons.append(schedule_of_lessons.pop(i))
                else:
                    schedule_of_lessons.insert(index_2+1, schedule_of_lessons.pop(i))
            elif (f"{second_lesson}-Exercise") in schedule_of_lessons:
                i = schedule_of_lessons.index(f"{second_lesson}-Exercise")
                if index_2 == -1:
                    schedule_of_lessons.append(schedule_of_lessons.pop(i))
                else:
                    schedule_of_lessons.insert(index_1+1, schedule_of_lessons.pop(i))
    elif command[0] == 'Exercise':
        lesson_title = command[1]
        if lesson_title in schedule_of_lessons:
            if (f"{lesson_title}-Exercise") not in schedule_of_lessons:
                index_of_lesson = schedule_of_lessons.index(lesson_title)
                schedule_of_lessons.insert(index_of_lesson+1,(f"{lesson_title}-Exercise"))
        else:
            schedule_of_lessons.append(lesson_title)
            schedule_of_lessons.append(f"{lesson_title}-Exercise")
    command = input()
if command == 'course start':
    for index, number in enumerate(schedule_of_lessons):
        print(f"{index + 1}.{number}")







