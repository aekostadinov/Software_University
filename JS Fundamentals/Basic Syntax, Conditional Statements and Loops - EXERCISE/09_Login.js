// You will be given a string representing a username. The correct password will be that username 
// reversed. Until you receive the correct password print on the console: "Incorrect password. Try 
// again.". When you receive the correct password print: "User {username} logged in." 
// However, on the fourth try if the password is still not correct print: "User {username} blocked!" 
// and end the program. The input comes as an array of strings - the first string represents username 
// and each subsequent string is a password.


function login(input) {
    let username = input.shift();
    let reversedUsername = username.split("").reverse().join("");
    let countFails = 0
    let currentLogin = input.shift();
    let itsBlocked = false
    while (currentLogin !== reversedUsername) {
        countFails ++
        if (countFails > 3) {
            console.log(`User ${username} blocked!`)
            itsBlocked = true
            break;
        }
        console.log("Incorrect password. Try again.")
        currentLogin = input.shift();
    }
    if (itsBlocked != true) {
        console.log(`User ${username} logged in.`)
    }
    
}
    

login(['momo','omom'])