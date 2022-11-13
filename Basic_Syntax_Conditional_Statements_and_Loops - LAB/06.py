budget = int(input())
command = input()

while not command == "End":
    num = int(command)
    if budget < num:
        print("You went in overdraft!")
        break
    budget -= num
    command = input()
if command == 'End':
    print("You bought everything needed.")


