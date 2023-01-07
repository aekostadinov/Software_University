// Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип от 
// продадените билети: студентски(student), стандартен(standard) и детски(kid), за всички прожекции.
// Трябва да изчислите и колко процента от залата е запълнена за всяка една прожекция.

// Вход
// Входът е поредица от цели числа и текст:
//     -На първия ред до получаване на командата "Finish" - име на филма – текст
//     -На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
//     -За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване 
// на командата "End":
//         oТипа на закупения билет - текст ("student", "standard", "kid")


function solve(input) {
    let nameMovie = input.shift();
    let totalTicket = 0;
    let studentCounter = 0;
    let standardCounter = 0;
    let kidsCounter = 0;
    while (nameMovie !== 'Finish') {
        let freeSpace = Number(input.shift());
        let typeTicket = input.shift();
        let sellsTicket = 0;
        while (typeTicket !== 'End') {
            if (typeTicket === 'student') {
                studentCounter++;
            } else if (typeTicket === 'standard') {
                standardCounter++;
            } else {
                kidsCounter++;
            }
            totalTicket++;
            sellsTicket++;
            if (sellsTicket >= freeSpace) {
                break;
            }
            typeTicket = input.shift();
        }
        console.log(`${nameMovie} - ${((sellsTicket / freeSpace) * 100).toFixed(2)}% full.`);
        nameMovie = input.shift();
    }
    console.log(`Total tickets: ${totalTicket}`);
    console.log(`${((studentCounter / totalTicket) * 100).toFixed(2)}% student tickets.`);
    console.log(`${((standardCounter / totalTicket) * 100).toFixed(2)}% standard tickets.`);
    console.log(`${((kidsCounter / totalTicket) * 100).toFixed(2)}% kids tickets.`);
}

// solve(["The Matrix",
// "20",
// "student",
// "standard",
// "kid",
// "kid",
// "student",
// "student",
// "standard",
// "student",
// "End",
// "The Green Mile",
// "17",
// "student",
// "standard",
// "standard",
// "student",
// "standard",
// "student",
// "End",
// "Amadeus",
// "3",
// "standard",
// "standard",
// "standard",
// "Finish"])