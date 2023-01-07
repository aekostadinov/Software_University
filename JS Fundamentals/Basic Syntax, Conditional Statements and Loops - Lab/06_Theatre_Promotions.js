// A theatre is doing a ticket sale, but they need a program to calculate the price of a single ticket. 
// If the given age does not fit one of the categories, you should print "Error!".  You can see the 
// prices in the table below:

function theatrePrice(day, age) {
    if (age < 0 || age > 122) {
        console.log("Error!")
    } else if  (day == "Weekday") {
        if ((0 <= age && age<= 18) || (64 < age && age <= 122)) {
            console.log("12$")
        } else if (18 < age && age<= 64) {
            console.log("18$")
        }
    } else if (day == "Weekend") {
        if ((0 <= age && age <= 18) || (64 < age && age <= 122)) {
            console.log("15$")
        } else if (18 < age && age<= 64) {
            console.log("20$")
        }
    } else if (day == "Holiday") {
        if (0 <= age && age<= 18) {
            console.log("5$")
        } else if (18 < age && age<= 64) {
            console.log("12$")
        } else if (64 < age && age<= 122) {
            console.log("10$")
        }
    }
}

