function sumNumbers(input) {
    let entryPoint = Number(input[0]);
    let result = 0;
    let index = 1
    while (result < entryPoint) {
        let currentNum = Number(input[index])
        result += currentNum
        index ++
    }
    console.log(result)
}