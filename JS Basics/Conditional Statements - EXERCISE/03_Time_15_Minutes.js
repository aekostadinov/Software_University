// Да се напише функция, която получава час и минути от 24-часово денонощие и изчислява колко ще
// е часът след 15 минути. Резултатът да се отпечата във формат часове:минути. Часовете винаги са 
// между 0 и 23, а минутите винаги са между 0 и 59. Часовете се изписват с една или две цифри. 
// Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо. 


function checkTime(input) {
    let hours = Number(input[0])
    let minutes = Number(input[1])
    let totalMinutes = hours * 60 + minutes + 15
    hours = Math.floor(totalMinutes / 60)
    if (hours >= 24)
        hours = 0
    minutes = totalMinutes % 60
    if (minutes <= 9)
        console.log(`${hours}:0${minutes}`)
    else
        console.log(`${hours}:${minutes}`)
}

checkTime(["23", "59"])
