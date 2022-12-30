// Петър иска да купи N видеокарти, M процесора и P на брой рам памет. Ако броя на видеокартите е по-голям 
// от този на процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
//     -Видеокарта – 250 лв./бр.
//     -Процесор – 35% от цената на закупените видеокарти/бр.
//     -Рам памет – 10% от цената на закупените видеокарти/бр.
// Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.

function neededMoney(input) {
    let budget = Number(input[0])
    let numbersVC = Number(input[1])
    let numbersCores = Number(input[2])
    let numbersRam = Number(input[3])
    let totalPriceVC = 250 * numbersVC
    let priceCore = totalPriceVC * 0.35
    let priceRam = totalPriceVC * 0.1
    let result = totalPriceVC + numbersCores * priceCore + numbersRam * priceRam
    if (numbersVC > numbersCores) {
        result *= 0.85
    }
    if (budget >= result) {
        let moneyLeft = budget - result
        console.log(`You have ${moneyLeft.toFixed(2)} leva left!`)
    }
    else{
        let moneyNeed = result - budget
        console.log(`Not enough money! You need ${moneyNeed.toFixed(2)} leva more!`)
    }

}

neededMoney((["900",
"2",
"1",
"3"]))

