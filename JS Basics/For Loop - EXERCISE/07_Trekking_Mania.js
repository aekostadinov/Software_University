// Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване. Според размера на 
// групата, катерачите ще изкачват различни върхове.
//     -Група до 5 човека – изкачват Мусала
//     -Група от 6 до 12 човека – изкачват Монблан
//     -Група от 13 до 25 човека – изкачват Килиманджаро
//     -Група от 26 до 40 човека –  изкачват К2
//     -Група от 41 или повече човека – изкачват Еверест
// Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.

function trekking(input) {
    let numbersGroup = Number(input[0]);
    let musala = 0
    let monblan = 0
    let kilimandzaro = 0
    let k2 = 0
    let everest = 0
    let numbersPeople = 0
    for (i = 1; i <= numbersGroup; i++) {
        let groupCount = Number(input[i])
        numbersPeople += groupCount
        if (groupCount <= 5) {
            musala += groupCount
        } else if (groupCount >= 6 && groupCount <= 12) {
            monblan += groupCount
        } else if (groupCount >= 13 && groupCount <= 25) {
            kilimandzaro += groupCount
        } else if (groupCount >= 26 && groupCount <= 40) {
            k2 += groupCount
        } else if (groupCount >= 41) {
            everest += groupCount
        } 
    }
    console.log(`${((musala/numbersPeople)*100).toFixed(2)}%`)
    console.log(`${((monblan/numbersPeople)*100).toFixed(2)}%`)
    console.log(`${((kilimandzaro/numbersPeople)*100).toFixed(2)}%`)
    console.log(`${((k2/numbersPeople)*100).toFixed(2)}%`)
    console.log(`${((everest/numbersPeople)*100).toFixed(2)}%`)
}

// trekking(["10",
// "10",
// "5",
// "1",
// "100",
// "12",
// "26",
// "17",
// "37",
// "40",
// "78"])