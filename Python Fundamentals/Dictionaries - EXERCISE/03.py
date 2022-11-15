country_names = input().split(", ")
capitals_names = input().split(", ")

dict_country_to_capitals = dict(zip(country_names,capitals_names))
for key, value in dict_country_to_capitals.items():
    print(f"{key} -> {value}")



