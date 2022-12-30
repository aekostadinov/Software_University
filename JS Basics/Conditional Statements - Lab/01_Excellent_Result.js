// Първата задача от тази тема е да се напише функция, която чете оценка, получена като аргумент и отпечатва "Excellent!", 
// ако оценката е 5.50 или по-висока.


function excellentGrade(input){
    let grade = Number(input[0])
    if (grade >= 5.5) {
        console.log("Excellent!")
    }
}

// excellentGrade(["6"]);