"""A palindrome is a number that reads the same backward as forward, such as 323 or 1001. Write a function
that receives a list of positive integers, separated by comma and space ", ". The function should check if
each integer is a palindrome - True or False. Print the result."""

def palindrome_checker(all_numbers):
    result = [True if number == number[::-1] else False for number in all_numbers]
    return result
    # result = []
    # for number in all_numbers:
    #     if number == number[::-1]:
    #         result.append(True)
    #     else:
    #         result.append(False)
    # return result


numbers = input().split(", ")
final_result = palindrome_checker(numbers)
for boolean in final_result:
    print(boolean)