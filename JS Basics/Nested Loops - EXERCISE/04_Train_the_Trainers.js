// Курсът "Train the trainers" е към края си и финалното оценяване наближава. Вашата задача е да помогнете на журито,  
// което ще оценява презентациите, като напишете функция,  която да изчислява средната оценка от представянето на всяка 
// една презентация от даден студент, а накрая средният успех от всички тях.
// От първия елемент на масива се прочита броят на хората в журито n - цяло число в интервала [1…20]
// След това името на презентацията - текст
// За всяка една презентация като нов елемент се чете n - на брой оценки - реално число в интервала [2.00…6.00]
// След изчисляване на средната оценка за конкретна презентация, на конзолата се печата
//  "{името на презентацията} - {средна оценка}."
// След получаване на команда "Finish" на конзолата се печата "Student's final assessment is {среден успех от всички 
// презентации}." и програмата приключва.
// Всички оценки трябва да бъдат форматирани до втория знак след десетичната запетая.

function trainers(input) {
    let countPeople = Number(input[0]);
    let index = 1;
    let namePresentation = input[index];
    let totalSum = 0
    let countPresentation = 0
    while (namePresentation != "Finish") {
        let currentSum = 0
        for (let i = 1; i <= countPeople; i++) {
            let currentGrade = Number(input[index + i])
            currentSum += currentGrade
        } 
        let averageGrade = currentSum / countPeople
        totalSum += averageGrade;
        countPresentation += 1
        console.log(`${namePresentation} - ${averageGrade}.`)  
        index += countPeople + 1
        namePresentation = input[index]
        if (namePresentation == "Finish") {
            break
        }
    }
    result = totalSum / countPresentation
    console.log(`Student's final assessment is ${(result).toFixed(2)}.`)
}   

trainers(["2",
"While-Loop",
"6.00",
"5.50",
"For-Loop",
"5.84",
"5.66",
"Finish"])