function hotelRoom(input) {
    let month = input[0]
    let countNights = Number(input[1])
    let apPrice
    let studioPrice
    if (month == 'May'|| month == 'October'){
        apPrice = 65
        studioPrice = 50
        if (countNights > 7 && countNights <=14 ) {
            studioPrice *= 0.95
        } else if (countNights > 14) {
            studioPrice *= 0.7
        }
    } else if (month == 'June'|| month == 'September'){
        apPrice = 68.7
        studioPrice = 75.2
        if (countNights > 14) {
            studioPrice *= 0.8
        }
    } else if (month == 'July'|| month == 'August'){
        apPrice = 77
        studioPrice = 76
    }
    if (countNights > 14) {
        apPrice *= 0.9
    }
    let apFinalSum = countNights * apPrice
    let studioFinalSum = countNights * studioPrice
    console.log(`Apartment: ${apFinalSum.toFixed(2)} lv.`)
    console.log(`Studio: ${studioFinalSum.toFixed(2)} lv.`)
}

hotelRoom(["June",
"14"])