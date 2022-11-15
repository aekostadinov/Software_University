command = input()
resource_dict = {}

while not command == 'stop':
    resource = command
    quantity = int(input())
    if resource not in resource_dict:
        resource_dict[resource] = 0
    resource_dict[resource] += quantity
    command = input()
for resource, quantity in resource_dict.items():
    print(f"{resource} -> {quantity}")
