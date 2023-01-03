// Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
// Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си. Напишете функция,
// която чете от масив по колко стъпки изминава тя всеки път като излиза през деня и когато постигне целта си да се 
// изписва "Goal reached! Good job!" и колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"
// Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките, които е извървяла докато 
// се прибира. След което, ако не е успяла да постигне целта си, на конзолата трябва да се изпише: "{разликата между 
// стъпките} more steps to reach goal."


function stepsCount(input) {
    let stepsGoal = 10000
    let currentSteps = 0
    let index = 0 
    while (currentSteps < stepsGoal) {
        let step = input[index]
        if (step == "Going home") {
            step = Number(input[index + 1]);
            currentSteps += step;
            break;
        } else {
            step = Number(input[index]);
            currentSteps += step;
        }
            if (currentSteps >= stepsGoal) {
            break;
        }
        index ++
    }
    if (currentSteps >= stepsGoal) {
        let stepsLeft = currentSteps - stepsGoal
        console.log(`Goal reached! Good job!`)
        console.log(`${stepsLeft} steps over the goal!`)
    } else {
        let stepsNeeded = stepsGoal - currentSteps
        console.log(`${stepsNeeded} more steps to reach goal.`)
    }
}

// stepsCount(["1500",
// "3000",
// "250",
// "1548",
// "2000",
// "Going home",
// "2000"])