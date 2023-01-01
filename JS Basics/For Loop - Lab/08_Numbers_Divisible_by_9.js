// Напишете функция, която получава две числа и принтира  на конзолата, всички числа в диапазона, които се 
// делят на 9 без остатък, както и тяхната сума.  На първия ред отпечатайте сумата на числата, а на следващите
// редове отговарящите на условието числа.

function numbersDivisible(input) {
    let firstNum = Number(input[0])
    let secondNum = Number(input[1])
    let sumNumbers = 0
    let result = ''
    for (num = firstNum; num <= secondNum; num += 1) {
        if (num % 9 == 0) {
            sumNumbers += num;
            result += num + "\n";
        }
    }
    console.log(`The sum: ${sumNumbers}`)
    console.log(result)
}

// numbersDivisible(["100", "200"])