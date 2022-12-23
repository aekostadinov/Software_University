"""First, you will be given two sequences of integers values on different lines. The values of the sequences
are separated by a single space between them.Keep in mind that each sequence should contain only unique values.
Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
    -"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
    -"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
    -"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
    -"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
    -"Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise,
print "False".
In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be
sorted in ascending order."""


def add_first():
    for num in numbers:
        first_sequence.add(num)
    return first_sequence


def add_second():
    for num in numbers:
        second_sequence.add(num)
    return second_sequence


def remove_first():
    for num in numbers:
        if num in first_sequence:
            first_sequence.remove(num)
    return first_sequence


def remove_second():
    for num in numbers:
        if num in second_sequence:
            second_sequence.remove(num)
    return second_sequence

def check_subset():
    if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
        print(True)
    else:
        print(False)

first_sequence = {int(num) for num in input().split()}
second_sequence = {int(num) for num in input().split()}
count_of_lines = int(input())
for _ in range(count_of_lines):
    command = input()
    numbers = [int(num) for num in command.split() if num.isdigit()]
    if command.startswith('Add First'):
        add_first()
    elif command.startswith('Add Second'):
        add_second()
    elif command.startswith('Remove First'):
        remove_first()
    elif command.startswith('Remove Second'):
        remove_second()
    elif command == 'Check Subset':
        check_subset()
first_seq_result = sorted(num for num in first_sequence)
second_seq_result = sorted(num for num in second_sequence)
print(', '.join(str(num) for num in first_seq_result))
print(', '.join(str(num) for num in second_seq_result))
