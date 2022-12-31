function priceProducts(input) {
    let product = input[0]
    let day = input[1]
    let quantity = Number(input[2])
    let price = 0
    let bul = true
    if (day == 'Monday' || day == 'Tuesday' || day == 'Wednesday' || day == 'Thursday' || day == 'Friday') {
        if (product == 'banana'){
            price = 2.5
        } else if (product == 'apple'){
            price = 1.2
        }else if (product == 'orange'){
            price = 0.85
        }else if (product == 'grapefruit'){
            price = 1.45
        }else if (product == 'kiwi'){
            price = 2.7
        }else if(product == 'pineapple'){
            price = 5.5
        }else if (product == 'grapes'){
            price = 3.85
        } else {
            bul = False
        }
        
    }
    else if (day == 'Saturday' || day == 'Sunday') {
        if (product == 'banana'){
            price = 2.7
        } else if (product == 'apple'){
            price = 1.25
        }else if (product == 'orange'){
            price = 0.9
        }else if (product == 'grapefruit'){
            price = 1.6
        }else if (product == 'kiwi'){
            price = 3
        }else if (product == 'pineapple'){
            price = 5.6
        }else if (product == 'grapes'){
            price = 4.2
        }
    }
    else {
        bul = false
    }
    if (bul != true){
        console.log('error')
    }
    else {
        let result = (quantity * price).toFixed(2)
        console.log(result);
    }
}



priceProducts(["orange",
"Sunday",
"3"])