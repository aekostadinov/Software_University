"""You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder
(0, 10, 20, 30...). Your task is to create a function that returns a loading bar depending on the number you
have received in the input. Print the result on the console. For more clarification, see the examples below."""

percentage_loaded = int(input())

def loading_bar(percentage):
    percentage_symbols = percentage // 10
    dot_symbols = 10 - percentage_symbols
    bar = f"{percentage}% [{percentage_symbols * '%'}{dot_symbols * '.'}]"
    if percentage in range(0, 100):
        return f"{bar}\nStill loading..."
    elif percentage == 100:
        return f"100% Complete!\n[{percentage_symbols * '%'}]"


result = loading_bar(percentage_loaded)
print(result)