// Напишете функция, която получава цяло число n и отпечатва пирамида от числа, като в примерите:

function pyramidNumbers(input) {
    let number = Number(input[0])
    let result = ''
    let current = 1   
    let isBigger = false
    for (let rows = 1; rows <= number; rows++) {
        for (let cols = 1; cols <= rows; cols++){
            if (current > number) {
                isBigger = true
                break;
            }
            result += current + " ";
            current++
        }
        console.log(result)
        result = ""
        if (isBigger) {
            break;
        }
    }
}

// pyramidNumbers(["7"])