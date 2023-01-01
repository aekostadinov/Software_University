// Да се напише функция, която получава число n и печата четните степени на 2 ≤ 2n: 20, 22, 24, 26, …, 2n.

function evenPowers(input) {
    let num = Number(input[0])
    let n = 0
    for (let n = 0 ; n <= num ; n += 2) {
        console.log(2 ** n);
    }
}

evenPowers(["7"])