from collections import deque

textfiles = deque(int(num) for num in input().split())  # first
medicaments = deque(int(num) for num in input().split())  # last
items_dict = {"Patch": 0, "Bandage": 0, "MedKit": 0}
while textfiles and medicaments:
    current_textfile = textfiles[0]
    current_medicament = medicaments[-1]
    current_sum = current_medicament + current_textfile
    if current_sum == 30:
        textfiles.popleft()
        medicaments.pop()
        items_dict["Patch"] += 1
    elif current_sum == 40:
        textfiles.popleft()
        medicaments.pop()
        items_dict["Bandage"] += 1
    elif current_sum == 100:
        textfiles.popleft()
        medicaments.pop()
        items_dict["MedKit"] += 1
    elif current_sum > 100:
        adding_sum = current_sum - 100
        items_dict["MedKit"] += 1
        textfiles.popleft()
        medicaments.pop()
        medicaments[-1] += adding_sum
    else:
        textfiles.popleft()
        medicaments[-1] += 10
if not textfiles and medicaments:
    print("Textiles are empty.")
if not medicaments and textfiles:
    print("Medicaments are empty.")
if not medicaments and not textfiles:
    print("Textiles and medicaments are both empty.")
if items_dict:
    sorted_dict = dict(sorted(items_dict.items(),key=lambda x: (-x[1],x[0])))
    for key,value in sorted_dict.items():
        if value != 0:
            print(f"{key} - {value}")
if medicaments:
    medicaments = list(reversed(medicaments))
    print(f"Medicaments left: {', '.join(str(el) for el in medicaments)}")
if textfiles:
    print(f"Textiles left: {', '.join(str(el) for el in textfiles)}")






