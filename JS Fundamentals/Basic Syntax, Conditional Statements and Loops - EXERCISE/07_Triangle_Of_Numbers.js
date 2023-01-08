// Write a function, which receives a single number – n, and prints a triangle from 1 to n as in 
// the examples.

function triangleNumbers(number) {
    for (let x = 1 ; x<=number; x++) {
        let result = ''
        for (let y = 1; y <= x; y++) {
            result += `${x} `  
        }
        console.log(result)
    }
}
// triangleNumbers(5)