// Марин и Нели си купуват къща не далеч от София. Нели толкова много обича цветята, че Ви убеждава да напишете 
// функция, която да изчисли колко  ще им струва, да си засадят определен брой цветя и дали наличния бюджет ще им
// е достатъчен. Различните цветя са с различни цени. 

// цвете	                Роза	Далия	Лале	Нарцис	Гладиола
// Цена на брой в лева	    5	    3.80	2.80	3	    2.50

// Съществуват следните отстъпки:
//     -Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена
//     -Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена
//     -Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена
//     -Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%
//     -Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%
// Функцията получава 3 аргумента:
//     -Вид цветя - текст с възможности - "Roses", "Dahlias", "Tulips", "Narcissus", "Gladiolus"
//     -Брой цветя - цяло число в интервала [10…1000]
//     -Бюджет - цяло число в интервала [50…2500]
// Да се отпечата на конзолата на един ред:
//     -Ако бюджета им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left."
//     -Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more."
// Сумата да бъде форматирана до втория знак след десетичната запетая.


function budgetNeeded(input) {
    let typeFlower = input[0]
    let numbersFlowers = Number(input[1])
    let budget = Number(input[2])
    let price
    if (typeFlower == "Roses") {
        price = 5
    } else if (typeFlower == "Dahlias") {
        price = 3.8
    } else if (typeFlower == "Tulips") {
        price = 2.8
    } else if (typeFlower == "Narcissus") {
        price = 3
    } else if (typeFlower == "Gladiolus") {
        price = 2.5
    }
    let totalSum = price * numbersFlowers
    if (typeFlower == 'Roses' && numbersFlowers > 80){
        totalSum *= 0.9
    } else if (typeFlower == 'Dahlias' && numbersFlowers > 90){
        totalSum *= 0.85
    } else if (typeFlower == 'Tulips' && numbersFlowers > 80){
        totalSum *= 0.85
    } else if (typeFlower == 'Narcissus' && numbersFlowers < 120){
        totalSum *= 1.15
    } else if (typeFlower == 'Gladiolus' && numbersFlowers < 80){
        totalSum *= 1.20
    }
    if (budget >= totalSum ) {
        let moneyLeft = budget - totalSum
        console.log(`Hey, you have a great garden with ${numbersFlowers} ${typeFlower} and ${moneyLeft.toFixed(2)} leva left.`)
    } else {
        let moneyNeed = totalSum - budget
        console.log(`Not enough money, you need ${moneyNeed.toFixed(2)} leva more.`)
    }
}