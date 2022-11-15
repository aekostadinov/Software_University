items = {"shards": 0, "fragments": 0, "motes": 0}
item_obtained = False
command_line = input().split()
while not item_obtained:
    for index in range(0, len(command_line), 2):
        quantity = int(command_line[index])
        item = command_line[index + 1].lower()
        if item not in items:
            items[item] = 0
        items[item] += quantity
        if items['shards'] >= 250:
            print("Shadowmourne obtained!")
            item_obtained = True
            items['shards'] -= 250
        elif items['fragments'] >= 250:
            print("Valanyr obtained!")
            item_obtained = True
            items['fragments'] -= 250
        elif items['motes'] >= 250:
            print("Dragonwrath obtained!")
            item_obtained = True
            items['motes'] -= 250
        if item_obtained:
            break
    if item_obtained:
        break
    command_line = input().split()
for key,value in items.items():
    print(f"{key}: {value}")



