console_words = input().split()
searched_word = input()
palindrome_list = [element for element in console_words if element[0::] == element[::-1]]
count = palindrome_list.count(searched_word)
print(palindrome_list)
print(f"Found palindrome {count} times")

