"""Write a program that reads the path to a file and subtracts the file name and its extension."""

### Variant 1 ###
text_list = input().split("\\")
for word in text_list:
    if "." in word:
        file_name, file_extension = word.split(".")
        print(f"File name: {file_name}\nFile extension: {file_extension}")


### Variant 2 ###
# text = input().split('\\')
# for word in text:
#     if "." in word:
#         subtracted_list = word.split('.')
#         print(f"File name: {subtracted_list[0]}\nFile extension: {subtracted_list[1]}")