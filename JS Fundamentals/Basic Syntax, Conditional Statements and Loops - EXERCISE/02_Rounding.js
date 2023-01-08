// Write a JS function that rounds numbers to a specific precision.
// The input comes as two numbers. The first value is the number to be rounded and the second is the 
// precision (significant decimal places). If the passed precision is more than 15, it should 
// automatically be reduced to 15.Remove trailing zeroes, if any (you can use parseFloat (number))
// The output should be printed to the console. Do not print insignificant decima

function rounding(number, precision) {
    let parsedNumber
    if (precision < 16 ) {
        result = number.toFixed(precision)
        parsedNumber = parseFloat(result)
    } else {
        result = number.toFixed(15)
        parsedNumber = parseFloat(result)
    }
    console.log(parsedNumber)
}
// rounding(10.5,3)