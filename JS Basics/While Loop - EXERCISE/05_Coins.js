// Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто. 
// Напишете функция, която приема сума - рестото, което трябва да се върне и изчислява с колко най-малко монети 
// може да стане това. Монетите може да са от 2 лева, 1 лев, 50 стотинки, 20 стотинки, 10 стотинки, 5 стотинки, 
// 2 стотинки или 1 стотинка.

function vendingMachine(input) {
    let coins = Math.round(input.shift() * 100);
    let numberCoins = 0
    while (coins > 0) {
        if (coins > 200) {
            coins -= 200
        } else if (coins >= 100) {
            coins -= 100
        }else if (coins >= 50) {
            coins -= 50
        } else if (coins >= 20) {
            coins -= 20
        } else if (coins >= 10) {
            coins -= 10
        } else if (coins >= 5) {
            coins -= 5
        } else if (coins >= 2) {
            coins -= 2
        } else if (coins >= 1) {
            coins -= 1
        } numberCoins += 1
    }
    console.log(numberCoins)
}

// vendingMachine(["1.23"])
// vendingMachine(["2.73"])