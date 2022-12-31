// Предприемчив българин отваря квартални магазинчета в няколко града и продава на различни цени според града:
// град / продукт	coffee	water	beer	sweets	peanuts
// Sofia	        0.50	0.80	1.20	1.45	1.60
// Plovdiv	        0.40	0.70	1.15	1.30	1.50
// Varna	        0.45	0.70	1.10	1.35	1.55
// Напишете функция, която получава аргументи: продукт (низ), град (низ) и количество (число), 
// и пресмята и отпечатва колко струва съответното количество от избрания продукт в посочения град. 


function price(input) {
    let product = input[0]
    let town = input[1]
    let quantity = Number(input[2])
    let priceProduct = 0
    if (town == "Sofia"){
        if (product == "coffee"){
            priceProduct = 0.5
        }else if (product == "water"){
            priceProduct = 0.8
        }else if (product == "beer"){
            priceProduct = 1.2
        }else if (product == "sweets"){
            priceProduct = 1.45
        }else if (product == "peanuts"){
            priceProduct = 1.6
        }
    } else if (town == "Plovdiv"){
        if (product == "coffee"){
            priceProduct = 0.4
        }else if (product == "water"){
            priceProduct = 0.7
        }else if (product == "beer"){
            priceProduct = 1.15
        }else if (product == "sweets"){
            priceProduct = 1.3
        }else if (product == "peanuts"){
            priceProduct = 1.5
        }
    } else if (town == "Varna"){
        if (product == "coffee"){
            priceProduct = 0.45
        }else if (product == "water"){
            priceProduct = 0.7
        }else if (product == "beer"){
            priceProduct = 1.1
        }else if (product == "sweets"){
            priceProduct = 1.35
        }else if (product == "peanuts"){
            priceProduct = 1.55
        }
    }
    let result = priceProduct * quantity
    console.log(result)
}

// price(["coffee",
// "Varna",
// "2"])