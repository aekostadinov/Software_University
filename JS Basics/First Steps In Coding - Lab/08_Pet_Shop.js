function petFood(input) {
    let dog_food = Number(input[0])
    let cat_food = Number(input[1])
    let price = dog_food * 2.5 + cat_food * 4
    console.log(`${price} lv.`)
}


petFood(["5","4"]);