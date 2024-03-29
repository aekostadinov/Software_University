"""Write a function called naughty_or_nice_list which will receive
    -A list representing Santa Claus' "Naughty or Nice" list full of kids' names
    -A different number of arguments (strings) and/or keywords representing commands
The function should sort the kids in the given Santa Claus list into 3 lists: "Nice", "Naughty", and "Not found".
The list holds a different number of kids - tuples containing two elements: a counting number (integer) at the first
position and a name (string) at the second position.
For example: [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")].
Next, the function could receive arguments and/or keywords.
Each argument is a command. The commands could be the following:
    -"{counting_number}-Naughty" - if there is only one tuple in the given list with the same number, MOVE the kid to a
list with NAUGHTY kids and remove it from the Santa list. Otherwise, ignore the command.
    -"{counting_number}-Nice" - if there is only one tuple in the given list with the same number, MOVE the kid to a
list with NICE kids and remove it from the Santa list. Otherwise, ignore the command.
Each keyword holds a key with a name (string), and each value will be a string ("Naughty" or "Nice"):
    -If there is only one tuple with the same name, MOVE the kid to a list with NAUGHTY or to the list with NICE kids
depending on the value in the keyword. Then, remove it from the Santa list.
    -Otherwise, ignore the command.
All remaining tuples in the given Santa's list are not found kids, and they should be MOVED to the "Not found" list.
In the end, return the final lists, each on a new line as described below.
Note: Submit only the function in the judge system

Input
    -There will be no input. Just parameters passed to your function.

Output
    -The function should return strings with the names on each list on separate lines, if there are any, otherwise skip
the line:
        o"Nice: {name1}, {name2} … {nameN}"
        o"Naughty: {name1}, {name2} … {nameN}"
"Not found: {name1}, {name2} … {nameN}"""


def naughty_or_nice_list(kids_names, *args, **kwargs):
    kids_dict = {"Nice": [], "Naughty": [], "Not found": []}
    result = ''
    if args:
        for command in args:
            counting_number, kid_type = [int(el) if el.isdigit() else el for el in command.split("-")]
            founded_tuple = None
            count_of_same_numbers = 0
            for tuple_ in kids_names:
                if counting_number == tuple_[0]:
                    count_of_same_numbers += 1
                    founded_tuple = tuple_
            if count_of_same_numbers == 1:
                kids_dict[kid_type].append(founded_tuple[1])
                kids_names.remove(founded_tuple)
    if kwargs:
        for name, type in kwargs.items():
            founded_tuple = None
            count_of_same_numbers = 0
            for tuple_ in kids_names:
                if name == tuple_[1]:
                    count_of_same_numbers += 1
                    founded_tuple = tuple_
            if count_of_same_numbers == 1:
                kids_dict[type].append(founded_tuple[1])
                kids_names.remove(founded_tuple)
    if kids_names:
        for tuple_ in kids_names:
            kids_dict["Not found"].append(tuple_[1])
    if kids_dict['Nice']:
        result += f"Nice: {', '.join(kids_dict['Nice'])}\n"
    if kids_dict['Naughty']:
        result += f"Naughty: {', '.join(kids_dict['Naughty'])}\n"
    if kids_dict['Not found']:
        result += f"Not found: {', '.join(kids_dict['Not found'])}\n"
    return result


# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))
