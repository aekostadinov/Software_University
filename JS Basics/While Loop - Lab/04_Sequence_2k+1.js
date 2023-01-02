// Напишете програма, която чете число n, въведено от потребителя и отпечатва всички числа ≤ n от редицата:
// 1, 3, 7, 15, 31, …. Всяко следващо число се изчислява като умножим предишното с 2 и добавим 1.

function numsSequence(input) {
    let data = Number(input[0])
    let result = 1
    while (result <= data) {
        console.log(result)
        result = result * 2 + 1
    }
}

