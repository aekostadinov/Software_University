"""You are given a collection of tickets separated by commas and spaces (one or many).
You need to check each ticket to see if it has a winning combination of symbols:

· A valid ticket has exactly 20 characters.
· A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' uninterruptedly
repeated at least 6 times in both halves of the tickets.
· In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides

An example of a valid winning ticket:

"Cash$$$$$$Ca$$$$$$sh"

An example of a Jackpot winning valid ticket:

"$$$$$$$$$$$$$$$$$$$$"

Input

The input will be read from the console. The input consists of a single line containing all
tickets separated by commas and one or more white spaces in the format:
· "{ticket}, {ticket}, … {ticket}"

Output

Print the result for every ticket in the order of their appearance, each on a separate line in the format:
· If the ticket is invalid: "invalid ticket
· If the ticket is valid, but it is not winning: "ticket "{ticket}" - no match"
· If the ticket is valid and winning, but not a Jackpot:
"ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}"
· It the ticket hits the Jackpot:
"ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!"""




text_sequence = input().replace(" ","")
text_sequence = text_sequence.split(",")
winning_symbols = ['@','#','$','^']
repetition = 0
winning_symbol = ''

for element in text_sequence:
    ticket_jackpot = False
    ticket_winner = False
    if len(element) != 20:
        print("invalid ticket")
        continue
    else:
        left_part = element[:10]
        right_part = element[10:]
        for symbol in winning_symbols:
            if symbol in left_part and symbol in right_part:
                for num in range(10, 5, -1):
                    if num * symbol in left_part and num * symbol in right_part:
                        winning_symbol = symbol
                        if num == 10:
                            ticket_jackpot = True
                            break
                        else:
                            repetition = num
                            ticket_winner = True
                            break
    if ticket_jackpot:
        print(f'ticket "{element}" - 10{winning_symbol} Jackpot!')
    elif ticket_winner:
        print(f'ticket "{element}" - {repetition}{winning_symbol}')
    else:
        print(f'ticket "{element}" - no match')
    repetition = 0
    winning_symbol = ''










