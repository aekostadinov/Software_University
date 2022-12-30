// Дадено е цяло число – начален брой точки. Върху него се начисляват бонус точки по правилата,
// описани по-долу. Да се напише функция, която пресмята бонус точките, които получава числото и 
// общия брой точки (числото + бонуса).
//     -Ако числото е до 100 включително, бонус точките са 5.
//     -Ако числото е по-голямо от 100, бонус точките са 20% от числото.
//     -Ако числото е по-голямо от 1000, бонус точките са 10% от числото.

//     -Допълнителни бонус точки (начисляват се отделно от предходните):
//         oЗа четно число  + 1 т.
//         oЗа число, което завършва на 5  + 2 т.

function bonusPoints(input) {
    let bonusPoints = 0
    let entryPoints = Number(input[0])
    if (entryPoints <= 100)
        bonusPoints = 5
    else if (entryPoints > 100 && entryPoints < 1000)
        bonusPoints = entryPoints * 0.2
    else if (entryPoints > 1000)
        bonusPoints = entryPoints * 0.1
    if (entryPoints % 2 == 0)
        bonusPoints += 1
    else if (entryPoints % 10 == 5)
        bonusPoints += 2
    let totalPoints = bonusPoints + entryPoints
    console.log(bonusPoints)
    console.log(totalPoints)
}

bonusPoints(["20"])