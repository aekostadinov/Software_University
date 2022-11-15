shuffle_cards = input().split()
count_of_shuffle = int(input())
new_shuffle_cards = []

for _ in range(count_of_shuffle):
    left_shuffle = shuffle_cards[:int(len(shuffle_cards) / 2)]
    right_shuffle = shuffle_cards[int(len(shuffle_cards) / 2):]
    new_shuffle_cards.clear()
    for i in range(int(len(left_shuffle))):
        new_shuffle_cards.append(left_shuffle[i])
        new_shuffle_cards.append(right_shuffle[i])
    shuffle_cards = new_shuffle_cards
print(shuffle_cards)
