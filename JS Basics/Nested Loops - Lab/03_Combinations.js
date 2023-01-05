// Напишете функция, която изчислява колко решения в естествените числа (включително и нулата) има уравнението:
// x1 + x2 + x3 = n
// Числото n е цяло число и се въвежда от конзолата. 

function combination(input) {
    let number = Number(input[0])
    let countSolutions = 0
    for (let x = 0; x <= number; x++) {
        for (let y = 0; y <= number; y++) {
            for (let z = 0; z <= number; z++) {
                if (x + y + z == number) {
                    countSolutions += 1
                }
            }
        }
    } console.log(countSolutions)
}

// combination(["25"])