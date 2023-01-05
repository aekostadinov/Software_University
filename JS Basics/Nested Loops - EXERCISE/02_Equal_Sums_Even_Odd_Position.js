// Напишете функция, която получава две шестцифрени цели числа в диапазона от 100000 до 300000. Винаги първото
// въведено число ще бъде по малко от второто. На конзолата да се отпечатат на 1 ред разделени с интервал всички числа, 
// които се намират между двете, прочетени от конзолата числа и отговарят на следното условие:
// сумата от цифрите на четни и нечетни позиции да са равни. Ако няма числа, отговарящи на условието на конзолата не 
// се извежда резултат. 

function checkSums(input) {
    let firstBoundary = Number(input[0]);
    let secondBoundary = Number(input[1]);
    let sumOdds = 0;
    let sumEvens = 0;
    let result = ''
    for (let num = firstBoundary; num <= secondBoundary; num++) {
        num = String(num);
        for (let element = 0; element < num.length; element++) {
            if (element % 2 == 0) {
                sumEvens += Number(num[element])
            } else if (element % 2 == 1) {
                sumOdds += Number(num[element])
            }
        } 
        if (sumEvens == sumOdds) {
            result += (`${num} `)
        }
        sumEvens = 0
        sumOdds = 0
    }
    console.log(result)
}

// checkSums(["100000",
// "100050"])