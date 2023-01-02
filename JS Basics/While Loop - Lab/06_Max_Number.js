// Напишете функция, която до получаване на командата "Stop", чете цели числа и намира най-голямото измежду тях. 
// Въвежда се по едно число на ред.

function maxNumber(input) {
    let entryBaseNumber = -Number.MAX_VALUE
    let index = 0
    while (input[index] != "Stop") {
        let currentNum = Number(input[index])
        if (currentNum > entryBaseNumber) {
            entryBaseNumber = currentNum
        }
        index ++
    }
    console.log(entryBaseNumber)

}

maxNumber(["-1",
"-2",
"Stop"])