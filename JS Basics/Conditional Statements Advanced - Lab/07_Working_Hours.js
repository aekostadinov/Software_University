// Да се напише функция, която получава час от денонощието(цяло число) и ден от седмицата(текст) и 
// проверява дали офисът на фирма е отворен, като работното време на офисът е от 10-18 часа, от понеделник 
// до събота включително.

function checkOffice(input){
    let hour = Number(input[0])
    let day = input[1]
    if ((day == 'Monday' || day == 'Tuesday' || day == 'Wednesday' || day == 'Thursday' || day == 'Friday' || day == 'Saturday') && (hour >= 10 && hour <= 18)) {
        console.log("open");
    }else{
        console.log("closed")
    }
}

// checkOffice(["11",
// "Monday"])