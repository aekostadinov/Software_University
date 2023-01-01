// Шеф на компания забелязва че все повече служители прекарват  време в сайтове, които ги разсейват.  
// За да предотврати това, той въвежда изненадващи проверки на отворените табове на браузъра на служителите си. 
// Според отворения сайт в таба се налагат следните глоби:
//     -"Facebook" -> 150 лв.
//     -"Instagram" -> 100 лв.
//     -"Reddit" -> 50 лв.
// От конзолата се четат два реда:
//     -Брой отворени табове в браузъра n - цяло число в интервала [1...10]
//     -Заплата - число в интервала [500...1500]
// След това n – на брой пъти се чете име на уебсайт – текст

function checkSalary(input) {
    let info = input
    let countSites = Number(input[0])
    let salary = Number(input[1])
    for (let i = 2; i < info.length; i++) {
        let currentSite = info[i]
        if (currentSite == "Facebook") {
            salary -= 150
        } else if (currentSite == "Instagram") {
            salary -= 100
        } else if (currentSite == "Reddit") {
            salary -= 50
        } if (salary <= 0) {
            console.log("You have lost your salary.")
            break
        }
    }
    if (salary > 0) {
        console.log(`${salary}`)
    }
}


// checkSalary(["3",
// "500",
// "Github.com",
// "Stackoverflow.com",
// "softuni.bg"])