"""Write a program that reads usernames on a single line (separated by ", ")
and prints all valid usernames on separate lines.

A valid username:
· has length between 3 and 16 characters inclusive
· can contain only letters, numbers, hyphens, and underscores
· has no redundant symbols before, after, or in between"""



def no_redundant_symbol(username):
    if ' ' in username:
        return False
    return True


def lenght_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def valid_characters(username):
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def username_is_valid(username):
    if valid_characters(username) and lenght_is_valid(username) and no_redundant_symbol(username):
        return True
    return False


usernames = input().split(", ")
for name in usernames:
    if username_is_valid(name):
        print(name)