"""On the first line, you will receive a sequence of numbers, each representing an egg with its size. On the second
line, you will receive another sequence of numbers, each representing a piece of paper with its size.
You should take the first egg and wrap it with the last piece of paper. Then, try to put it in a box with a size of 50.
Each wrapped-in-a-paper egg fills one box if it fits in it. Your task is to check whether you have filled at least one box.
You should comply with the following conditions:
    -If the egg is not fresh anymore (its size is less than or equal to 0), you need to remove it from the sequence before
it is wrapped with a piece of paper.
    -If the sum of the egg's size and the paper's size is less than or equal to the box's size (50), put the wrapped egg in
the box and remove both from the sequences.
        oOtherwise, you cannot fill a box, so remove both the egg and the paper from the sequences without putting them in a box.
    -During your work, you noticed that Old MacDonald is superstitious. If the size of an egg is 13 it brings bad luck to
him. You should remove this egg from the sequence before it is wrapped with a piece of paper.
        oFurthermore, each time you take an egg with a size of 13, it will be best to swap the first and last pieces of paper
positions to bring the good luck back to Old MacDonald.
        Note: There will be NO case where there will be just one piece of paper left.
For more clarification see the examples below.

Input
    -In the first line, you will be given a sequence of eggs with their sizes - integers separated by comma and space ", "
 in the range [-100, 100]
    -In the second line, you will be given a sequence of pieces of paper with their sizes - integers separated by comma and
 space ", " in the range [1, 100]

Output
    -On the first line:
        oIf you have at least one box filled, print:
        "Great! You filled {total count} boxes."
        oIf you couldn't fill any boxes, print:
        "Sorry! You couldn't fill any boxes!"
    -On the following lines, print the eggs left or pieces of paper left if there are any:
    oEggs left: {left eggs joined by ", "}
    oPieces of paper left: {left pieces of paper joined by ", "}"""

from collections import deque

eggs_size = deque(int(num) for num in input().split(", "))
piece_of_paper_size = deque(int(num) for num in input().split(", "))

count_of_boxes = 0

while (eggs_size and piece_of_paper_size):
    current_egg = eggs_size.popleft()
    current_piece_of_papper = piece_of_paper_size.pop()
    if current_egg <= 0:
        piece_of_paper_size.append(current_piece_of_papper)
        continue
    elif current_egg == 13:
        piece_of_paper_size.append(piece_of_paper_size.popleft())
        piece_of_paper_size.appendleft(current_piece_of_papper)
        continue
    sum = current_egg + current_piece_of_papper
    if sum <= 50:
        count_of_boxes += 1
if count_of_boxes > 0:
    print(f"Great! You filled {count_of_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs_size:
    print(f"Eggs left: {', '.join(str(el) for el in eggs_size)}")
if piece_of_paper_size:
    print(f"Pieces of paper left: {', '.join(str(el) for el in piece_of_paper_size)}")

