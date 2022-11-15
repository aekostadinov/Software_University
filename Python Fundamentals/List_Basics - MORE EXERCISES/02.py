sequence_number = input().split()
given_string = input()
current_sum = 0
output_string = ''
bul = False

for i in range(len(sequence_number)):
    for j in range(len(sequence_number[i])):
        current_sum += int(sequence_number[i][j])
    if current_sum < len(given_string):
        bul = True
    elif current_sum >= len(given_string):
        current_sum = current_sum % len(given_string)
        bul = True
    if bul:
        output_string += given_string[current_sum]
        given_string = given_string[:current_sum] + given_string[current_sum + 1:]
        current_sum = 0

print(output_string)








