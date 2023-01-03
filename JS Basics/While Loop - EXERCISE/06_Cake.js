// Поканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта. Той обаче не знае колко парчета могат
// да си вземат гостите от нея. Вашата задача е да напишете функция, която изчислява броя на парчетата, които гостите 
// са взели, преди тя да свърши. Ще получите размерите на тортата (широчина и дължина – цели числа в интервала [1...1000])
// и след това на всеки ред, до получаване на командата "STOP" или докато не свърши тортата, броят на парчетата, които 
// гостите вземат от нея.

// Бележка: Едно парче торта е с размер 1х1 см.
// Да се отпечата на конзолата един от следните редове:
//     -"{брой парчета} pieces are left." - ако стигнете до STOP и не са свършили парчетата торта
//     -"No more cake left! You need {брой недостигащи парчета} pieces more."

function cakePieces(input) {
    let lenght = Number(input[0])
    let width = Number(input[1])
    let totalPieces = lenght * width
    let index = 2
    let currentCount = input[index]
    while (true) {
        if (currentCount == 'STOP') {
            console.log(`${totalPieces} pieces are left.`)
            break;
        }
        currentCount = Number(input[index])
        totalPieces -= currentCount
        if (totalPieces < 0) {
            console.log(`No more cake left! You need ${-totalPieces} pieces more.`)
            break;
        }
        index ++
        currentCount = input[index]
    }
    
}

// cakePieces(["10",
// "10",
// "20",
// "20",
// "20",
// "20",
// "21"])