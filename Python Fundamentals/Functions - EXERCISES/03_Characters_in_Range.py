"""Write a function that receives two characters and returns a single string with all the characters in between them
 (according to the ASCII code), separated by a single space. Print the result on the console"""

def characters_in_between(start_index, end_index):
    start_index = ord(start_index) + 1
    end_index = ord(end_index)
    result = [chr(character) for character in range(start_index, end_index)]
    return result


starting_letter = input()
ending_letter = input()
# print(' '.join(characters_in_between(starting_letter, ending_letter)))
final_result = characters_in_between(starting_letter, ending_letter)
print(' '.join(final_result))