// Write a function that displays numbers from given start to given end and their sum. The input 
// comes as two number parameters. Print the result like the examples below:

function printSum(first, second) {
    let result = ''
    let sum = 0
    for (let i = first; i <= second; i++) {
        result += `${i} `
        sum += i
    }
    console.log(result)
    console.log(`Sum: ${sum}`)
}

// printSum(5,10)