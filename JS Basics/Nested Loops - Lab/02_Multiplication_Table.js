// Отпечатайте на конзолата таблицата за умножение за числата от 1 до 10 във формат: 
// "{първи множител} * {втори множител} = {резултат}". 

function multiplication() {
    for (let firstNum = 1; firstNum <= 10; firstNum++) {
        for (let secondNum = 1; secondNum <= 10; secondNum++) {
            result = firstNum * secondNum
            console.log(`${firstNum} * ${secondNum} = ${result}`)
        }
    }
}

