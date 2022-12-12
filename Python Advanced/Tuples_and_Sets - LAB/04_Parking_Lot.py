"""Write a program that:
· Records a car number for every car that enters the parking lot
· Removes a car number when the car leaves the parking lot

On the first line, you will receive the number of commands - N. On the following N lines, you will receive the
direction and car's number in the format: "{direction}, {car_number}". The direction could only be "IN" or "OUT".
Print the car numbers which are still in the parking lot. Keep in mind that all car numbers must be unique.
If the parking lot is empty, print "Parking Lot is Empty".

Note: The order in which we print the result does not matter."""


count = int(input())
set_of_numbers = set()

for _ in range(count):
    information = tuple(input().split(", "))
    direction, car_number = information
    if direction == 'IN':
        set_of_numbers.add(car_number)
    else:
        set_of_numbers.remove(car_number)
if set_of_numbers:
    for number in set_of_numbers:
        print(number)
else:
    print("Parking Lot is Empty")

