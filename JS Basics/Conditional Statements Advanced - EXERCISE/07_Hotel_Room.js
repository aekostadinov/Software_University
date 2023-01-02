// Хотел предлага 2 вида стаи: студио и апартамент. Напишете функция, която изчислява цената за целия престой за
// студио и апартамент. Цените зависят от месеца на престоя:
// Май и октомври	                Юни и септември             	Юли и август
// Студио – 50 лв./нощувка	        Студио – 75.20 лв./нощувка	    Студио – 76 лв./нощувка
// Апартамент – 65 лв./нощувка	    Апартамент – 68.70 лв./нощувка	Апартамент – 77 лв./нощувка
// Предлагат се и следните отстъпки:
//     -За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
//     -За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
//     -За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
//     -За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

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

// hotelRoom(["June",
// "14"])