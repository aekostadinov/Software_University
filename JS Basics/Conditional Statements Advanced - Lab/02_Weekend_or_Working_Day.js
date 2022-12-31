// Напишете функция която, чете ден от седмицата (текст), на английски език - въведен от потребителя. Ако денят 
// е работен отпечатва на конзолата - "Working day", ако е почивен - "Weekend". Ако се въведе текст различен от
//  ден от седмицата да се отпечата - "Error".


function dayOfWeek(input) {
    day = input[0];
    switch (day) {
        case "Monday":
        case "Tuesday":
        case "Wednesday":
        case "Thursday":
        case "Friday":
            console.log("Working day");break
        case "Saturday":
        case "Sunday":
            console.log("Weekend");break
        default:
            console.log("Error");break
    }
}