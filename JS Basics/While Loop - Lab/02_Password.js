// Напишете функция, която първоначално прочита име и парола на потребителски профил. След това чете парола за вход. 
// при въвеждане на грешна парола: потребителя да се подкани да въведе нова парола.
// при въвеждане на правилна парола: отпечатваме "Welcome {username}!".

function password(input) {
    let user = input[0]
    let password = input[1]
    let index = 2 
    while (true) {
        let newPassword = input[index]
        if (newPassword == password) {
            console.log(`Welcome ${user}!`);
            break;
        }
        index ++
    }
}