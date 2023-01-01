// Дадени са n цели числа в интервала [1…1000]. От тях някакъв процент p1 са под 200,
// друг процент p2 са от 200 до 399, друг процент p3 са от 400 до 599, друг процент p4 
// са от 600 до 799 и останалите p5 процента са от 800 нагоре. Да се напише програма, 
// която изчислява и отпечатва процентите p1, p2, p3, p4 и p5.

function histogram(input) {
    let numberDigits = Number(input[0])
    let numbersSequence = input
    let p1,p2,p3,p4,p5 = 0;0;0;0;0

    for (let i = 1; i < numbersSequence.length; i++){
        let num = Number(input[i])
        if (num < 200) {
            p1 += 1
        }else if (num <= 399) {
            p2 += 1
        }else if (num <= 599) {
            p3 += 1
        }else if (num <= 799) {
            p4 += 1
        }else if (num >= 800) {
            p5 += 1
        }
    }
    console.log(`${((p1/numberDigits)* 100).toFixed(2)}%`)
    console.log(`${((p2/numberDigits)* 100).toFixed(2)}%`)
    console.log(`${((p3/numberDigits)* 100).toFixed(2)}%`)
    console.log(`${((p4/numberDigits)* 100).toFixed(2)}%`)
    console.log(`${((p5/numberDigits)* 100).toFixed(2)}%`)
}

histogram(["3",
"1",
"2",
"999"])
