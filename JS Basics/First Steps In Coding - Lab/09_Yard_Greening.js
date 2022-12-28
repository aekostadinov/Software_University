function gardenPrice(input) {
    let sq_meters = Number(input[0])
    let price_without_discount = sq_meters * 7.61
    let discount = 0.18 * price_without_discount
    let final_price = price_without_discount - discount
    console.log(`The final price is: ${final_price} lv.`)
    console.log(`The discount is: ${discount} lv.`)
}


gardenPrice(["550"]);