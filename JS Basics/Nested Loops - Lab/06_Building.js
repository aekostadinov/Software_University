// Напишете функция, която извежда на конзолата номерата на стаите в една сграда (в низходящ ред), като са изпълнени 
// следните условия:
//     -На всеки четен етаж има само офиси
//     -На всеки нечетен етаж има само апартаменти
//     -Всеки апартамент се означава по следния начин : А{номер на етажа}{номер на апартамента}, номерата на апартаментите
// започват от 0.
//     -Всеки офис се означава по следния начин : О{номер на етажа}{номер на офиса}, номерата на офисите също започват от 0.
//     -На последният етаж винаги има апартаменти и те са по-големи от останалите, за това пред номера им пише 'L', 
// вместо 'А'. Ако има само един етаж, то има само големи апартаменти!
// Функцията получава масив от две цели числа - броят на етажите и броят на стаите за един етаж. 

function building(input) {
    let result = ''
    let numberFloors = Number(input[0])
    let numberRooms = Number(input[1])
    for (let floor = numberFloors; floor >= 1; floor--) {
        for (let room = 0; room < numberRooms; room++) {
            if (floor == numberFloors) {
                result += (`L${floor}${room} `)
            } else if (floor % 2 == 0) {
                result += (`O${floor}${room} `)
            } else if (floor % 2 != 0) {
                result += (`A${floor}${room} `)
            }
        }
        result += "\n"
    } console.log(result)
}

// building(["6", "4"])
