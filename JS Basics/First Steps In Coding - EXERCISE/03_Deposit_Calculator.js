// Напишете програма, която изчислява каква сума ще получите в края на депозитния период при определен лихвен процент. 
// Използвайте следната формула: сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

function finalSum(input) {
    let depositedSum = Number(input[0]);
    let time = Number(input[1]);
    let precentPerYear = Number(input[2]);
    let finalSum = depositedSum + time * ((depositedSum * precentPerYear/100)/12);
    console.log(finalSum);
}

finalSum(["2350","6 ","7"]);