// Напишете функция, която получава аргумент число от 1 до 10 и принтира таблицата за умножение в конзолата. 

function multiplicationTable(input) {
    number = Number(input[0])
    let result = 0
    for (let i = 1; i <= 10; i++){
        result = number * i
        console.log(`${i} * ${number} = ${result}`)
    }
}