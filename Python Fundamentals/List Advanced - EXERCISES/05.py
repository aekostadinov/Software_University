number_of_rooms = int(input())
room = 0
empty_chairs = 0
bul = True

for _ in range(number_of_rooms):
    information = input().split(" ")
    free_chairs = information[0]
    visitors = int(information[1])
    room += 1
    if len(free_chairs) < visitors:
        needed_chairs = visitors - len(free_chairs)
        print(f"{needed_chairs} more chairs needed in room {room}")
        bul = False
    else:
        empty_chairs += len(free_chairs) - visitors
if bul > 0:
    print(f"Game On, {empty_chairs} free chairs left")




