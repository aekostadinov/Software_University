// Да се напише функция,  която получава като вида и размерите на геометрична фигура и пресмята лицето й. 
// Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle).
//  На първия ред на входа се чете вида на фигурата (текст със следните възможности: square, rectangle, circle или triangle). 
//     -Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
//     -Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
//     -Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
//     -Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и 
// дължината на височината към нея.Резултатът да се закръгли до 3 цифри след десетичната запетая. 



function area(input) {
    let shape = input[0]
    result = 0
    if (shape == 'square') {
        let side = Number(input[1])
        result= side * side
    }
    else if (shape == 'rectangle') {
        sideA = Number(input[1])
        sideB = Number(input[2])
        result = sideA * sideB
    }
    else if (shape == 'triangle') {
        base = Number(input[1])
        height = Number(input[2])
        result = base * height/2
    }
    else if (shape == 'circle') {
        radius = Number(input[1])
        result = Math.PI * radius * radius
    }
    console.log(result.toFixed(3));
}

area(["circle",
"6"])
