// През годината Гришо участва в определен брой турнири, като за всеки турнир получава точки, които зависят от 
// позицията, на която е завършил в турнира. Има три варианта за завършване на турнир:
//     -W - ако е победител получава 2000 точки
//     -F - ако е финалист получава 1200 точки
//     -SF - ако е полуфиналист получава 720 точки
// Напишете програма, която изчислява колко ще са точките на Григор след изиграване на всички турнири, като 
// знаете с колко точки стартира сезона. Също изчислете колко точки средно печели от всички изиграни турнири 
// и колко процента от турнирите е спечелил. 

// Вход
// От конзолата първо се четат два реда:
//     -Брой турнири, в които е участвал – цяло число в интервала [1…20] 
//     -Начален брой точки в ранглистата - цяло число в интервала [1...4000]
// За всеки турнир се прочита отделен ред:
//     -Достигнат етап от турнира – текст – "W", "F" или "SF"

// Изход
// Отпечатват се три реда в следния формат:
//     -"Final points: {брой точки след изиграните турнири}"
//     -"Average points: {средно колко точки печели за турнир}"
//     -"{процент спечелени турнири}%"
// Средните точки да бъдат закръглени към най-близкото цяло число надолу, а процентът да се форматира до втората 
// цифра след десетичния знак.


function tennisTournament(input) {
    let numbersTournaments = Number(input[0]);
    let entryPoints = Number(input[1]);
    let totalPoints = 0
    let countOfWins = 0
    for (i=2; i <= numbersTournaments + 2; i++) {
        let tournamentResult = input[i]
        if (tournamentResult == 'W') {
            totalPoints += 2000
            countOfWins += 1
        } else if (tournamentResult == 'F') {
            totalPoints += 1200
        } else if (tournamentResult == 'SF') {
            totalPoints += 720
        }
    } 
    console.log(`Final points: ${entryPoints + totalPoints}`)
    let averagePoints = (totalPoints / numbersTournaments)
    console.log(`Average points: ${Math.floor(averagePoints)}`)
    let precentOfWinns = (((countOfWins/numbersTournaments)*100).toFixed(2))
    console.log(`${precentOfWinns}%`)
}

tennisTournament(["5",
"1400",
"F",
"SF",
"W",
"W",
"SF"])