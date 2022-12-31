// Да се напише функция, която получава ден от седмицата (текст) и принтира на конзолата цената на билет 
// за кино според деня от седмицата:


// Monday	Tuesday	 Wednesday	Thursday	Friday	Saturday	Sunday
//   12	      12	    14	       14	      12	   16	      16

function solve(input) {
    day = input[0]
    if (day == 'Monday' || day == 'Tuesday' || day == 'Friday'){
        console.log(12)
    }else if (day == 'Wednesday' || day == 'Thursday'){
        console.log(14)
    }else{
        console.log(16)
    }
}