// Да се напише функция, която получава аргумент  име на продукт  и проверява дали е плод или зеленчук.
//     -Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes
//     -Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot
//     -Всички останали са "unknown"
// Да се изведе "fruit", "vegetable" или "unknown" според въведения продукт.


function checkProduct(input) {
    product = input[0]
    if (product == 'banana' || product == 'apple' || product == 'kiwi' || product == 'cherry' 
    || product == 'lemon' || product == 'grapes') {
        console.log("fruit")
    } else if (product == 'tomato' || product == 'cucumber' || product == 'pepper' || product == 'carrot') {
        console.log("vegetable")
    } else {
        console.log("unknown")
    }
}
