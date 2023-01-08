// You are given a group of people, the type of the group, and the day of the week they are going to 
// stay. Based on that information calculate how much they have to pay and print that price on the 
// console. Use the table below. In each cell is the price for a single person. 
// The output should look like that: `Total price: {price}`.The price should be formatted to the second 
// decimal point.
// There are also discounts based on some conditions:
//     ·Students – if the group is bigger than or equal to 30 people you should reduce the total price 
// by 15%
//     ·Business – if the group is bigger than or equal to 100 people 10 of them can stay for free
//     ·Regular – if the group is bigger than or equal to 10 and less than or equal to 20 reduce the 
// total price by 5%
// Note: You should reduce the prices in that EXACT order.


function vacation(people, typeGroup, dayWeek) {
    let pricePerPerson = 0
    if (dayWeek == "Friday" && typeGroup == "Students") {
        pricePerPerson = 8.45
    } else if (dayWeek == "Saturday" && typeGroup == "Students") {
        pricePerPerson = 9.8
    } else if (dayWeek == "Sunday" && typeGroup == "Students") {
        pricePerPerson = 10.46
    } else if (dayWeek == "Friday" && typeGroup == "Business") {
        pricePerPerson = 10.9
    } else if (dayWeek == "Saturday" && typeGroup == "Business") {
        pricePerPerson = 15.6
    } else if (dayWeek == "Sunday" && typeGroup == "Business") {
        pricePerPerson = 16
    } else if (dayWeek == "Friday" && typeGroup == "Regular") {
        pricePerPerson = 15
    } else if (dayWeek == "Saturday" && typeGroup == "Regular") {
        pricePerPerson = 20
    } else if (dayWeek == "Sunday" && typeGroup == "Regular") {
        pricePerPerson = 22.5
    }
    let totalPrice = people * pricePerPerson
    if (typeGroup == "Students" && people >= 30) {
        totalPrice *= 0.85
    } else if (typeGroup == "Business" && people >= 100) {
        totalPrice -= 10 * pricePerPerson
    } else if (typeGroup == "Regular" && people >= 10 && people <= 20) {
        totalPrice *= 0.95
    }
    console.log(`Total price: ${totalPrice.toFixed(2)}`)
}
// vacation(30,
// "Students",
// "Sunday")