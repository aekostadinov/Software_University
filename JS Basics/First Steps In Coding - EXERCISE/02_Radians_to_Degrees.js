// Напишете програма, която чете ъгъл в радиани (десетично число) и го преобразува в градуси.
// Използвайте формулата: градус = радиан * 180 / π. Числото π в Java програми е достъпно чрез
// Math.PI.

function radiansToDegrees(input) {
    let radians = Number(input[0]);
    let degrees = radians * 180/Math.PI;
    console.log(degrees);
}