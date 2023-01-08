// You will receive a number as a parameter. Print the 10 times table for this number. See the examples
// below for more information.

function multiplicationTable(number) {
    for (let i = 1 ; i <= 10; i++) {
        let result = number * i
        console.log(`${number} X ${i} = ${result}`)
    }
}