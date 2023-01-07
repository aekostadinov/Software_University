// Да се напише програма, която чете едно цяло число N, въведено от потребителя, и генерира всички 
// възможни "специални" числа от 1111 до 9999. За да бъде "специално" едно число, то трябва да отговаря
// на следното условие: 
//     -N да се дели на всяка една от неговите цифри без остатък.
// Пример: при N = 16, 2418 е специално число:
//     -16 / 2 = 8 без остатък
//     -16 / 4 = 4 без остатък
//     -16 / 1 = 16 без остатък
//     -16 / 8 = 2 без остатък

function specialNumbers(input) {
    
    let n = Number(input[0])
    result = ''
    for (number = 1111; number <= 9999; number ++) {
        let itsSpecial = true
        let numberAsString = String(number)
        for (let index = 0; index < numberAsString.length; index++) {
            let currentDigit = Number(numberAsString[index])
            if (n % currentDigit != 0) {
                itsSpecial = false
            }
        } if (itsSpecial) {
            result += (`${number} `)
        }
    }
    console.log(result)
}

specialNumbers(["3"])