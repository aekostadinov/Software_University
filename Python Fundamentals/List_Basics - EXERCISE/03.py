team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
bul = False
players_input = input().split()
for index in range(0, len(players_input)):
    if players_input[index] in team_a:
        team_a.remove(players_input[index])
    elif players_input[index] in team_b:
        team_b.remove(players_input[index])
    if len(team_a) < 7 or len(team_b) < 7:
        bul = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if bul:
    print("Game was terminated")

