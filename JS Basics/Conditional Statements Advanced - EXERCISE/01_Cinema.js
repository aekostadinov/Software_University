// В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони. Има три вида прожекции с билети на
// различни цени:
//     -Premiere – премиерна прожекция, на цена 12.00 лева.
//     -Normal – стандартна прожекция, на цена 7.50 лева.
//     -Discount – прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
// Напишете функция, която приема тип прожекция (стринг), брой редове и брой колони в залата (цели числа) и изчислява 
// общите приходи от билети при пълна зала. Резултатът да се отпечата във формат като в примерите по-долу, с 2 знака 
// след десетичната точка.  

function price(input) {
    let type = input[0]
    let countRows = Number(input[1])
    let countColumns = Number(input[2])
    let numberSeats = countRows * countColumns
    let result = 0
    if (type == 'Premiere') {
        result = numberSeats * 12
    }
    else if (type == 'Normal') {
        result = numberSeats * 7.5
    }
    else if (type == 'Discount') {
        result = numberSeats * 5
    }
    console.log(result.toFixed(2))
}