function lilyBirthday(input) {
    let age = Number(input[0]);
    let priceWashingMachine = Number(input[1]);
    let pricePerToy = Number(input[2]);
    let countToys = 0
    let money = 0
    let moneyGift = 10
    for (i = 1; i <= age; i++) {
        if (i % 2 == 1) {
            countToys += 1
        } else if (i % 2 == 0) {
            money += moneyGift - 1
            moneyGift += 10
        }
    }
    money += countToys * pricePerToy
    if (priceWashingMachine <= money) {
        let moneyLeft = money - priceWashingMachine
        console.log(`Yes! ${(moneyLeft).toFixed(2)}`)
    } else {
        let moneyNeed = priceWashingMachine - money
        console.log(`Yes! ${(moneyNeed).toFixed(2)}`)
    }
}

lilyBirthday(["21",
"1570.98",
"3"])