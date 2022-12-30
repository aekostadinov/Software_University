// Иван решава да подобри Световния рекорд по плуване на дълги разстояния. Функцията получава: рекордът в секунди,
// който Иван трябва да подобри,  разстоянието в метри, което трябва да преплува и времето в секунди, за което плува 
// разстояние от 1 м. Да се напише функция, която изчислява дали се е справил със задачата, като се има предвид, че: 
// съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди. Когато се изчислява колко пъти Иванчо ще се забави,
// в резултат на съпротивлението на водата, резултатът трябва да се закръгли надолу до най-близкото цяло число.
// Да се изчисли времето в секунди, за което Иванчо ще преплува разстоянието и разликата спрямо Световния рекорд. 


function SwimmerSeconds(input) {
    let recordSeconds = Number(input[0]);
    let lenghtMeters = Number(input[1]);
    let timePerMeter = Number(input[2]);
    let countOfLosses = Math.floor(lenghtMeters / 15)
    let secondsLoss = countOfLosses * 12.5
    let finalTime = lenghtMeters * timePerMeter + secondsLoss;
    if (finalTime < recordSeconds) {
        console.log(`Yes, he succeeded! The new world record is ${finalTime.toFixed(2)} seconds.`)
    }
    else{
        let neededSeconds = finalTime - recordSeconds
        console.log(`No, he failed! He was ${neededSeconds.toFixed(2)} seconds slower.`)
    }
}   

