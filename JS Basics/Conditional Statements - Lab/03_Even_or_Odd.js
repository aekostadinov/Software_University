// Да се напише  функция, която получава цяло число  като аргумент и отпечатва на конзолата,
// дали е четно или нечетно. Ако е четно отпечатайте "even", ако е нечетно "odd".


function evenOrOdd(input){
    let num =  Number(input[0])
    if (num % 2 == 0)
        console.log("even")
    else
        console.log("odd")
}

// evenOrOdd(["-1"]);