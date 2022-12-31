// Напишете функция, която получава  две цели числа (N1 и N2) и оператор, с който да се извърши дадена математическа
// операция с тях. Възможните операции са: Събиране(+), Изваждане(-), Умножение(*), Деление(/) и Модулно деление(%).
// При събиране, изваждане и умножение на конзолата трябва да се отпечатат резултата и дали той е четен или нечетен. 
// При обикновеното деление – резултата. При модулното деление – остатъка. Трябва да се има предвид, че делителят може 
// да е равен на 0(нула), а на нула не се дели. В този случай трябва да се отпечата специално съобщениe.

function operations(input) {
    firstNum = Number(input[0])
    secondNum = Number(input[1])
    operator = input[2]
    let result
    if (operator == '+') {
        result = firstNum + secondNum
    } else if (operator == '-') {
        result = firstNum - secondNum
    } else if (operator == '*') {
        result = firstNum * secondNum
    }
    if (operator == "+" || operator == "-" || operator == "*") {
        if (result % 2 == 0){
            console.log(`${firstNum} ${operator} ${secondNum} = ${result} - even`)
        } else {
            console.log(`${firstNum} ${operator} ${secondNum} = ${result} - odd`)
        }
    } else if (operator == '/') {
        if (secondNum == 0) {
            console.log(`Cannot divide ${firstNum} by zero`)
        } else {
            result = firstNum/secondNum
            console.log(`${firstNum} / ${secondNum} = ${result.toFixed(2)}`)
        }
    }  else if (operator == "%") {
        if (secondNum == 0) {
            console.log(`Cannot divide ${firstNum} by zero`)
        } else {
            result = firstNum % secondNum
            console.log(`${firstNum} % ${secondNum} = ${result}`)
        }
    }
}