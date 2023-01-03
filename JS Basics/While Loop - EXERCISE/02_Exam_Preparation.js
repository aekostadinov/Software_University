// Напишете функция, в която Марин решава задачи от изпити докато не получи съобщение "Enough" от лектора си. 
// При всяка решена задача той получава оценка. Функцията трябва да приключи прочитането на данни при команда 
// "Enough" или ако Марин получи определеният брой незадоволителни оценки.
// Незадоволителна е всяка оценка, която е по-малка или равна на 4.

// Вход
//     -На първи ред - брой незадоволителни оценки - цяло число в интервала [1…5]
//     -След това многократно се четат по два реда:
//         oИме на задача - текст (низ)
//         oОценка - цяло число в интервала [2…6]

// Изход
//     -Ако Марин стигне до командата "Enough", отпечатайте на 3 реда: 
//         o"Average score: {средна оценка}"
//         o"Number of problems: {броя на всички задачи}"
//         o"Last problem: {името на последната задача}"
//     -Ако получи определеният брой незадоволителни оценки:
//         o"You need a break, {брой незадоволителни оценки} poor grades."
// Средната оценка да бъде форматирана до втория знак след десетичната запетая. 

function examPreparation(input) {
    let countPoorGrades = Number(input[0])
    let taskName;
    let index = 1
    let sumPoorGrades = 0
    let sumAllGrades = 0
    let countofTasks = 0
    while (input[index] != "Enough") {
        taskName = input[index]
        let grade = Number(input[index + 1])
        if (grade <= 4) {
            sumPoorGrades += 1
            if (countPoorGrades == sumPoorGrades) {
                console.log(`You need a break, ${sumPoorGrades} poor grades.`);
                break;
            }
        }
        countofTasks += 1
        sumAllGrades += grade
        index += 2
    }
    if (input[index] == 'Enough') {
        let averageGrade = sumAllGrades / countofTasks
        console.log(`Average score: ${averageGrade.toFixed(2)}`)
        console.log(`Number of problems: ${countofTasks}`)
        console.log(`Last problem: ${taskName}`)
    }
}

// examPreparation(["3",
// "Money",
// "6",
// "Story",
// "4",
// "Spring Time",
// "5",
// "Bus",
// "6",
// "Enough"])