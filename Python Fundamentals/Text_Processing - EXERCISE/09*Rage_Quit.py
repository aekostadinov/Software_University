"""He'll give you a series of strings (containing only non-numerical characters) followed
by non-negative numbers (N), e.g., "a3". You need to convert the letters to uppercase for
each string and print it repeatedly N times on the console. In the example, you need to write back "AAA".
First, on the output, you should print a statistic of the number of unique symbols used
 (case-insensitive) in the format: "Unique symbols used {0}".

Next, print the rage message itself.
The strings and numbers will not be separated by anything. The input will always start with a
non-numeric symbol, and for each string, there will be a corresponding number. The input will
be given on a single line.

Input
· The input data should be read from the console.
· It consists of a single line holding a series of string-number sequences.
· The input data will always be valid. There is no need to check it explicitly.

Output
· The output should be printed on the console. It should consist of exactly two lines:
o On the first line, print the number of unique symbols used in the message in the format described above.
o On the second line, print the rage message."""



text = input().upper()
current_symbol = ''
repetition = ''
output = ''
for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index]
    else:
        for check_next_symbol in range(index,len(text)):
            if not text[check_next_symbol].isdigit():
                break
            repetition += text[check_next_symbol]
        repetition = int(repetition)
        output += current_symbol * repetition
        current_symbol = ''
        repetition = ''
print(f"Unique symbols used: {len(set(output))}")
print(output)

