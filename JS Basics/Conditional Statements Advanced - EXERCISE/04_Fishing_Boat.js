// Тони и приятели много обичали да ходят за риба, те са толкова запалени по риболова, че решават да отидат на
// риболов с кораб. Цената за наемане на кораба зависи от сезона и броя рибари.
// Цената зависи от сезона:
//     -Цената за наем на кораба през пролетта е  3000 лв.
//     -Цената за наем на кораба през лятото и есента е  4200 лв.
//     -Цената за наем на кораба през зимата е  2600 лв.
// В зависимост от броя си групата ползва отстъпка:
//     -Ако групата е до 6 човека включително  –  отстъпка от 10%.
//     -Ако групата е от 7 до 11 човека включително  –  отстъпка от 15%.
//     -Ако групата е от 12 нагоре  –  отстъпка от 25%. 
// Рибарите ползват допълнително 5% отстъпка ако са четен брой освен ако не е есен - тогава нямат допълнителна отстъпка. 
// Напишете функция, която да пресмята дали рибарите ще съберат достатъчно пари. 

function neededBudget(input) {
    let budget = Number(input[0])
    let season = input[1]
    let countFishers = Number(input[2])
    let rentPrice 
    if (season == 'Spring') {
        rentPrice = 3000
    } else if (season == 'Summer' || season == 'Autumn') {
        rentPrice = 4200
    } else if (season == 'Winter') {
        rentPrice = 2600
    }
    if (countFishers <= 6) {
        rentPrice *= 0.9
    } else if (countFishers >= 7 && countFishers <= 11) {
        rentPrice *= 0.85
    } else if (countFishers >= 12) {
        rentPrice *= 0.75
    }
    if (countFishers % 2 == 0 && season != "Autumn") {
        rentPrice *= 0.95
    }
    if (budget >= rentPrice) {
        let moneyLeft = budget - rentPrice
        console.log(`Yes! You have ${moneyLeft.toFixed(2)} leva left.`)
    } else {
        let moneyNeeded = rentPrice - budget
        console.log(`Not enough money! You need ${moneyNeeded.toFixed(2)} leva.`)
    }
}