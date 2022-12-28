"""Alex is a vlogger and he wants to make videos of climbing the five highest peaks in Pirin mountain in just one week.
He will take his video set, a tent, and his backpack to the mountain. The backpack fits food portions for one week,
exactly. His daily stamina is also limited. Your task is to trace his adventure and create a post for his profile
@alaroundtheworld, at the end of the journey.You will have to keep information for all the conquered peaks if any.
Every day, Alex will use one portion of his daily food supplies and will exhaust one of his daily stamina.
First, you will be given a sequence of numbers	, representing the quantities of the daily portions of food supplies
in his backpack.Afterward, you will be given another sequence of numbers, representing the quantities of the daily
stamina he will have at his disposal for the next seven days.You have to sum the quantity of the last daily food
portion with the quantity of the first daily stamina. He will start climbing from the first peak in the table
below to the last one.
    -If the sum is equal to or greater than the corresponding Mountain Peak’s Difficulty level from the table below,
it means that the peak is conquered. In this case, you should remove both quantities from the sequences and continue
with the next ones towards the next peak.
    -If the sum is less than the corresponding Mountain Peak’s Difficulty level from the table below, the peak remains
unconquered. You should remove both quantities from the sequences. Alex will have to sleep in his tent. On the next day,
he will try the same peak once again.

Mountain Peaks	Difficulty level
Vihren	        80
Kutelo	        90
Banski Suhodol	100
Polezhan	    60
Kamenitza	    70

Alex will try to conquer as many peaks as he can in seven days. If he manages to climb all the peaks, the journey ends
and the output is printed on the Console.Finally, print on the Console all the conquered peaks(in the order of climbing).

Input
    -On the first line, you will receive the food portions, separated by a comma and a single space (', ').
    -On the second line, you will receive the stamina, separated by a comma and a single space (', ').

Output
    -On the first line – print whether Alex managed to reach his goal and climb all the peaks in his list:
        oIf he managed to conquer all: "Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK"
        oIf he didn't manage to climb all of the peaks: "Alex failed! He has to organize his journey better next time
-> @PIRINWINS"
    -Then, in either case, you need to print all the conquered peaks (in the order of climbing) if any:
"Conquered peaks:
{peak1}
{peak2}
…
{peakn}"
    oIf there are no concurred peaks, do NOT print this message."""


from collections import deque

food_portions = deque([int(num) for num in input().split(", ")])  # last
stamina = deque([int(num) for num in input().split(", ")])  # first

mountain_information = {80: "Vihren", 90: "Kutelo", 100: "Banski Suhodol", 60: "Polezhan", 70: "Kamenitza"}
peaks = [80, 90, 100, 60, 70]
days = 0
conquered_peaks = []
while days <= 6:
    daily_food = food_portions.pop()
    daily_stamina = stamina.popleft()
    current_sum = daily_food + daily_stamina
    current_peak = peaks[0]
    if current_sum >= current_peak:
        value = peaks.pop(0)
        conquered_peaks.append(mountain_information[value])
    days += 1
    if not peaks:
        break
if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print("Conquered peaks:")
    for peak in conquered_peaks:
        print(peak)

