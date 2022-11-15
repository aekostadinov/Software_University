population = [int(number) for number in input().split(", ")]
minimum_wealth = int(input())
sum_of_population = sum(population)


if len(population) * minimum_wealth > sum(population):
    print("No equal distribution possible")
elif len(population) * minimum_wealth == sum(population):
    result = [minimum_wealth] * len(population)
    print(result)
else:
    for index in range(len(population)):
        max_number = max(population)
        if population[index] <= minimum_wealth:
            difference = minimum_wealth - population[index]
            population[index] = minimum_wealth
            index_of_maximum_number = population.index(max_number)
            population[index_of_maximum_number] -= difference
    print(population)
