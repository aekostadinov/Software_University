function timeCalculation(input) {
    let name = input[0]
    let projects = Number(input[1])
    let time = 3 * projects
    console.log(`The architect ${name} will need ${time} hours to complete ${projects} project/s.`)
}


timeCalculation(["George ","4 "]);