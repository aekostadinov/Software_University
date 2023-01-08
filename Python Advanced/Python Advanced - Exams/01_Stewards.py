"""You will be given a sequence of 6 seats - every seat is a mix of a number and a letter in the format
"{number}{letter}". You will also be given two more sequences of numbers only.
First, you have to take the first number of the first sequence and the last number of the second sequence. Next, take
the sum of those two numbers and find its ASCII character.
    -Compare each of the two taken numbers and the found character with the seats. If you find a match, the passenger is
seated, and the seat is considered taken. Remove both numbers from their sequences.
    -If there is no equality, the two numbers should be returned at the end of their sequences (first becomes last, last
becomes first).
    -If you match an already taken seat, you should just remove both numbers from their sequences.
Each time you take numbers from the sequences and try to match them, you make one rotation. You should keep track of
all rotations made.

The program should end under the following circumstances:
    -You have found 3 (three) seat matches
    -You have made a total of 10 rotations

Input
    -On the first line, you will be given a sequence of seats - strings separated by comma and space ", "
    -On the second and the third line, you will be given two more sequences - integers separated by a comma
and a space ", "

Output
When the program ends, print the following on two different lines:
oSeat matches: {matches separated by comma and space}
oRotations count: {total rotations made}"""



from collections import deque

sequence_of_seets = input().split(", ")
first_seq_of_nums = deque(int(num) for num in input().split(", "))
second_seq_of_nums = [int(num) for num in input().split(", ")]
seat_matches = []
rotation = 0
while rotation < 10:
    seat_found = False
    rotation += 1
    first_num = first_seq_of_nums.popleft()
    second_num = second_seq_of_nums.pop()
    sum_of_nums = first_num + second_num
    ascii_char = chr(sum_of_nums)
    first_concat = str(first_num) + ascii_char
    second_concat = str(second_num) + ascii_char
    if first_concat in sequence_of_seets:
        seat_matches.append(first_concat)
        seat_found = True
        sequence_of_seets.remove(first_concat)
    if second_concat in sequence_of_seets:
        seat_matches.append(second_concat)
        seat_found = True
        sequence_of_seets.remove(second_concat)
    if not seat_found:
        second_seq_of_nums.insert(0,second_num)
        first_seq_of_nums.append(first_num)
    if len(seat_matches) == 3:
        break

print(f"Seat matches: {(', '.join(el for el in seat_matches))}")
print(f"Rotations count: {rotation}")





