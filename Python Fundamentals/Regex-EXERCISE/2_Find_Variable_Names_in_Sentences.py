# import re
#
# text = input()
# pattern = r"(?<=\b_)[A-Za-z0-9]+\b"
#
# matched_words = re.findall(pattern, text)
# print(",".join(matched_words))



import re

text = input()
pattern = r"(?<=\b_)[A-Za-z0-9]+\b"

matched_words = [obj.group() for obj in re.finditer(pattern, text)]
print(",".join(matched_words))