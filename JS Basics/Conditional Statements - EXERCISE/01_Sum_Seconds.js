// Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50). Да се напише функция, която получава три 
// аргумента - секунди и пресмята сумарното им време във формат "минути:секунди". Секундите да се изведат с водеща нула 
// (2  "02", 7  "07", 35  "35"). 


function sumSeconds(input) {
    let firstPlayer = Number(input[0])
    let secondPlayer = Number(input[1])
    let thirdPlayer = Number(input[2])
    let sumOfSeconds = firstPlayer + secondPlayer + thirdPlayer
    let minutes = Math.trunc(sumOfSeconds/60)
    let seconds = sumOfSeconds % 60
    if (seconds <= 9)
        console.log(`${minutes}:0${seconds}`)
    else
        console.log(`${minutes}:${seconds}`)
}

sumSeconds(["22", "7", 
"34"])
