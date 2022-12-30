// По време на обедната почивка искате да изгледате епизод от своя любим сериал. Вашата задача е да напишете програма,
// с която ще разберете дали имате достатъчно време да изгледате епизода. По време на почивката отделяте време за обяд
// и време за отдих. Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка. 


function time(input) {
    let nameMovie = input[0]
    let timeMovie = Number(input[1])
    let timeRest = Number(input[2])
    let timeLunch = timeRest / 8
    let timeOtherStuff = timeRest / 4
    let spareTime = (timeRest - (timeLunch + timeOtherStuff))
    if (spareTime >= timeMovie) {
        let timeLeft = Math.ceil(spareTime - timeMovie)
        console.log(`You have enough time to watch ${nameMovie} and left with ${timeLeft} minutes free time.`)
    }
    else {
        let timeNeed = Math.ceil(timeMovie - spareTime)
        console.log(`You don't have enough time to watch ${nameMovie}, you need ${timeNeed} more minutes.`)
    }
}
time(["Teen Wolf",
"48",
"60"])
