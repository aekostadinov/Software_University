// Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни. С парите, 
// които ще спечели иска да отиде на екскурзия. 
// Цени на играчките:
//     -Пъзел - 2.60 лв.
//     -Говореща кукла - 3 лв.
//     -Плюшено мече - 4.10 лв.
//     -Миньон - 8.20 лв.
//     -Камионче - 2 лв.
// Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена. От спечелените пари
// Петя трябва да даде 10% за наема на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

function Money(input) {
    let priceTrip = Number(input[0])
    let numberPuzzles = Number(input[1])
    let numberDolls = Number(input[2])
    let numberBears = Number(input[3])
    let numberMinions = Number(input[4])
    let numberTrucks = Number(input[5])
    let numberToys = numberPuzzles + numberDolls + numberBears + numberMinions + numberTrucks
    let totalSum  = numberPuzzles * 2.6 + numberDolls * 3 + numberBears * 4.1 + numberMinions * 8.2 + numberTrucks * 2
    if (numberToys >= 50)
        totalSum = totalSum * 0.75
    let result = totalSum * 0.9
    if (totalSum >= priceTrip){
        let moneyLeft = result - priceTrip
        console.log(`Yes! ${moneyLeft} lv left.`)
    }
    else {
        let neededMoney = priceTrip - result
        console.log(`Not enough money! ${neededMoney.toFixed(2)} lv needed.`)
    }
}

// Money(["320",
// "8",
// "2",
// "5",
// "5",
// "1"])