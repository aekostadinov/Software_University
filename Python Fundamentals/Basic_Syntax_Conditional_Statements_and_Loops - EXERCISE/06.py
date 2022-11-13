n = int(input())

for _ in range(n):
    str_inp = input()
    if '.' in str_inp or ',' in str_inp or '_' in str_inp:
        print(f"{str_inp} is not pure!")
    else:
        print(f"{str_inp} is pure.")

