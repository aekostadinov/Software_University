// Поканени сте от академията да напишете софтуер, който да пресмята точките за актьор/актриса. Академията ще ви 
// даде първоначални точки за актьора. След това всеки оценяващ ще дава своята оценка. Точките, които актьора
// получава се формират от: дължината на името на оценяващия умножено по точките, които дава делено на две. 
// Ако резултатът в някой момент надхвърли 1250.5 програмата трябва да прекъсне и да се отпечата, че дадения
// актьор е получил номинация.

function oscars(input) {
    let nameActor = input[0];
    let pointsAcademy = Number(input[1]);
    let countJury = Number(input[2]);
    let totalPoints = pointsAcademy;
    for (let i=3; i< 3 + countJury * 2; i+=2) {
        let nameJury = input[i]
        let pointsJury = Number(input[i+1]);
        let currentLength = nameJury.length
        totalPoints += (currentLength * pointsJury / 2)
        if (totalPoints > 1250.5) {
            console.log(`Congratulations, ${nameActor} got a nominee for leading role with ${totalPoints.toFixed(1)}!`)
            break
        }
    }
    if (totalPoints <= 1250.5) {
        let neededPoints = 1250.5 - totalPoints
        console.log(`Sorry, ${nameActor} you need ${neededPoints.toFixed(1)} more!`)
    }

}

// oscars(["Sandra Bullock",
// "340",
// "5",
// "Robert De Niro",
// "50",
// "Julia Roberts",
// "40.5",
// "Daniel Day-Lewis",
// "39.4",
// "Nicolas Cage",
// "29.9",
// "Stoyanka Mutafova",
// "33"])