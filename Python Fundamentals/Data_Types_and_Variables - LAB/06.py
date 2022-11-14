current_year = int(input())
bul = False

while not bul:
    current_year += 1
    set_year = set()
    for i in range(len(str(current_year))):
        set_year.add(str(current_year)[i])

    bul = len(set_year) == len(str(current_year))

print(current_year)


