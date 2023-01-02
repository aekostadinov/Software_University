function graduation(input) {
    let studentName = input[0]
    let failedCounts = 0
    let grade = 1
    let sumGrades = 0
    while (grade <= 12) {
        let currentGrade = Number(input[grade])
        if (currentGrade < 4) {
            failedCounts += 1
            if (failedCounts == 2){
                console.log(`${studentName} has been excluded at ${grade-1} grade`);
                break;
            }
        }
        sumGrades += currentGrade
        grade ++
    }
    if (grade == 13) {
        let averageGrade = sumGrades / (grade - 1)
        console.log(`${studentName} graduated. Average grade: ${averageGrade.toFixed(2)}`)
    }
}

graduation(["Mimi", 
"5",
"6",
"5",
"6",
"5",
"6",
"6",
"2",
"3"])