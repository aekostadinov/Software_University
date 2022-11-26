"""You receive a string consisting of a number between two letters. For the given string, you should perform different mathematical operations to achieve a result:

· First, if the letter in front of the number is:

o Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
o Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)

· Next, if the letter after the number is:

o Uppercase: subtract its position from the resulting number (starting from 1)
o Lowercase: add its position to the resulting number (starting from 1)

The game was too easy for John. He decided to complicate it by doing the same calculations
to multiple strings keeping track of only the total sum of all results. Once he started
to solve this with more strings and bigger numbers, it became quite hard to do it only in his mind.
He kindly asks you to write a program that performs the operations described above and sums
the final results of each string.

Input

· The input comes from the console as a single line, holding a sequence of strings
· Strings are separated by one or more white spaces
· The input data will always be valid. There is no need to check it explicitly

Output

· Print at the console a single number:
o The total sum of all processed numbers, formatted to the second decimal separator"""


def alphabet_num(character):
    return (ord(character) - 96)


sequence_of_strings = input().split()
final_sum = 0
print(sequence_of_strings)
for element in sequence_of_strings:
    first_result = 0
    output_result = 0
    first_char = element[0]
    second_char = element[-1]
    number = int(element[1:-1])
    first_char_num_alphabet, second_char_num_alphabet = alphabet_num(first_char.lower()), alphabet_num(second_char.lower())
    if first_char.isupper():
        first_result = number / first_char_num_alphabet
    elif first_char.islower():
        first_result = number * first_char_num_alphabet
    if second_char.isupper():
        output_result = first_result - second_char_num_alphabet
    elif second_char.islower():
        output_result = first_result + second_char_num_alphabet
    final_sum += output_result
print(f"{final_sum:.2f}")



