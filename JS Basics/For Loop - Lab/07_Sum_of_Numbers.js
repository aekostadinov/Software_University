// Напишете функция, която получава цяло число n, сумира всички негови цифри и отпечатва сумата. 


function sumNumbers(input) {
    let number = input[0];
    let sumDigits = 0;
    for (i = 0; i < number.length; i++){
        let currentDigit = Number(number[i]);
        sumDigits += currentDigit;
    }
    console.log(`The sum of the digits is:${sumDigits}`);
}

// sumNumbers(["564891"])