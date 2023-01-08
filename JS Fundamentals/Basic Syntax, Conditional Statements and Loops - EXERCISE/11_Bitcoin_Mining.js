// Write a JavaScript program that calculates the total amount of bitcoins you purchased with 
// the gold you mined during your shift at the mine. Your shift consists of a certain number of 
// days where you mine an amount of gold in grams. Your program will receive an array with the 
// amount of gold you mined each day, where the first day of your shift is the first index of the 
// array. Also, someone was stealing every third day from the start of your shift 30% from the mined
// gold for this day. You need to check, which day you have enough money to buy your first bitcoin. 
// For the different exchanges use these prices:


function bitcoinMining(input) {
    let dayCounter = 0
    let btcPrice = 0
    let firstBuyDay
    let countBtc = 0
    let BtcBought = false
    while (input[0]) {
        dayCounter++
        let currentShift = input.shift()
        if (dayCounter % 3 == 0) {
            currentShift *= 0.7 
        }
        let currentShiftEarning = currentShift * 67.51
        btcPrice += currentShiftEarning
        if (btcPrice >= 11949.16) {
            if (BtcBought == false) {
                firstBuyDay = dayCounter
            BtcBought = true
            }
        }
    }
    countBtc = Math.floor(btcPrice / 11949.16)
    console.log(`Bought bitcoins: ${countBtc}`)
    if (countBtc > 0) {
        console.log(`Day of the first purchased bitcoin: ${firstBuyDay}`)
    }
    let moneyLeft = btcPrice - countBtc * 11949.16
    console.log(`Left money: ${moneyLeft.toFixed(2)} lv.`)
}
    
bitcoinMining([100, 200, 300])
