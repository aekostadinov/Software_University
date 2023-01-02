// Напишете функция, която чете елементите на масив, докато не получи командата "Stop".

function readText(input) {
    let index = 0
    while(true) {
        let str = input[index];
            if (str == 'Stop' ) {
                break;
            }
        console.log(str);
        index ++
    }
}

