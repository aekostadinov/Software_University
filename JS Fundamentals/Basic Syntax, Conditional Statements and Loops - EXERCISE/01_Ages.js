// Write a function that determines whether based on the given age a person is: baby, child, teenager, 
// adult, elder.

// The input comes as a single number parameter. The bounders are:

//     · 0-2 (age) – is a baby;
//     · 3-13 (age) – is a child;
//     · 14-19 (age) – is a teenager;
//     · 20-65 (age) – is an adult;
//     · >=66 (age) – is an elder;
//     · In all other cases print – "out of bounds";

// The output should be printed to the console

function age(number) {
    if (0 <= number && number <=2) {
        console.log("baby")
    } else if (3 <= number && number <=13) {
        console.log("child")
    } else if (14 <= number && number <=19) {
        console.log("teenager")
    } else if (20 <= number && number <=65) {
        console.log("adult")
    } else if (number >=66) {
        console.log("elder")
    } else {
        console.log("out of bounds")
    }
}

// age(20)