// Лято е с много променливо време и Виктор има нужда от вашата помощ. Напишете функция,  която спрямо времето от 
// денонощието и градусите да препоръча на Виктор какви дрехи да си облече. Вашия приятел има различни планове за 
// всеки етап от деня, които изискват и различен външен вид, тях може да видите от таблицата.
// Функцията получава два аргумента:
//     -Градусите - цяло число в интервала [10…42]
//     -Текст, време от денонощието - с възможности - "Morning", "Afternoon", "Evening"




function outfit(input) {
    let degree = Number(input[0])
    let time = input[1]
    let outfit
    let shoes
    if (degree >= 10 && degree <= 18) {
        if (time == "Morning") {
            outfit = "Sweatshirt"
            shoes = "Sneakers"
        } else if (time == "Afternoon" || time == "Evening") {
            outfit = "Shirt"
            shoes = "Moccasins"
        }
    }
    else if (degree > 18 && degree <= 24) {
        if (time == "Afternoon") {
            outfit = "T-Shirt"
            shoes = "Sandals"
        } else if (time == "Morning" || time == "Evening") {
            outfit = "Shirt"
            shoes = "Moccasins"
        }
    }
    else if (degree >= 25) {
        if (time == "Morning") {
            outfit = "T-Shirt"
            shoes = "Sandals"
        } else if (time == "Afternoon") {
            outfit = "Swim Suit"
            shoes = "Barefoot"
        } else if (time == "Evening") {
            outfit = "Shirt"
            shoes = "Moccasins"
        }
    }
    console.log(`It's ${degree} degrees, get your ${outfit} and ${shoes}.`)
}