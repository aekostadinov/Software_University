// Да се напише функция, която получава, изчислява и отпечатва сумата от стойностите на гласните букви
// според таблицата по-долу:

function vowelsSum(input) {
    let text = input[0];
    let vowels = 0;
    for (i = 0; i < text.length; i++) {
        let letter = text[i]
        if (letter == 'a') {
            vowels += 1
        } else if (letter == 'e') {
            vowels += 2
        } else if (letter == 'i') {
            vowels += 3
        } else if (letter == 'o') {
            vowels += 4
        } else if (letter == 'u') {
            vowels += 5
        } 
    }
    console.log(vowels)
}

// vowelsSum(["bamboo"])