// Странно, но повечето хора си плануват отрано почивката. Млад програмист разполага с определен бюджет и свободно 
// време в даден сезон. Напишете функция, която да получава бюджета и сезона и на изхода да изкарва, къде ще почива 
// програмистът и колко ще похарчи.Бюджета определя дестинацията, а сезона определя колко от бюджета ще изхарчи. 
// Ако е лято ще почива на къмпинг, а зимата в хотел. Ако е в Европа, независимо от сезона ще почива в хотел. 
// Всеки къмпинг или хотел, според дестинацията, има собствена цена която отговаря на даден процент от бюджета: 
//     -При 100лв. или по-малко – някъде в България
//         oЛято – 30% от бюджета
//         oЗима – 70% от бюджета
//     -При 1000лв. или по малко – някъде на Балканите
//         oЛято – 40% от бюджета
//         oЗима – 80% от бюджета
//     -При повече от 1000лв. – някъде из Европа
//         oПри пътуване из Европа, независимо от сезона ще похарчи 90% от бюджета.


function tripPrice(input) {
    budget = Number(input[0])
    season = input[1]
    let destination
    let price
    let place
    if (budget <= 100) {
        destination = "Bulgaria"
        if (season == 'summer') {
            price = 0.3 * budget
        } else if (season == 'winter') {
            price = 0.7 * budget
        }
    } else if (budget > 100 && budget <= 1000) {
        destination = "Balkans"
        if (season == 'summer') {
            price = 0.4 * budget
        } else if (season == 'winter') {
            price = 0.8 * budget
        }
    } else if (budget > 1000) {
        destination = "Europe"
        price = 0.9 * budget
    }
    if (season == 'summer' && destination != "Europe") {
        place = "Camp"
    } else {
        place = "Hotel"
    }
console.log(`Somewhere in ${destination}`)
console.log(`${place} - ${price.toFixed(2)}`)
    
}



