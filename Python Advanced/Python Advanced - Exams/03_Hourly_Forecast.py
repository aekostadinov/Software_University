"""Write a function called forecast that stores information about the weather, and returns sorted information for 
all locations. The function will receive a different number of arguments. The arguments will be passed as tuples 
with two elements - the first one is the location, and the second one is the weather:
    -Location name: string
        o any string
    -Weather: string
        o"Sunny"
        o"Rainy"
        o"Cloudy"
First, sort all locations by weather. First are positioned the locations with sunny weather, next are the locations
with cloudy weather, and last are the locations with rainy weather. For each sequence of locations (e.g. all sunny 
locations), sort them by their name in ascending order (alphabetically).
In the end, return the output as described below.
Note: Submit only the function in the judge system

Input
    -There will be no input from the console, just parameters passed to your function
Output
    -The output should look like this:
    "{first_sorted_location} - {weather}"
    "{second_sorted_location} - {weather}"
    …
    "{last_sorted_location} - {weather}"""

def forecast(*args):
    result = ''
    weather_locations = {"Sunny":[],"Cloudy":[],"Rainy":[]}
    for tup in args:
        location, weather = tup
        weather_locations[weather].append(location)
    for weather, locations in weather_locations.items():
        weather_locations[weather] = sorted(locations)
        for city in weather_locations[weather]:
            result += f"{city} - {weather}" + "\n"
    return result


# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))
#
# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))