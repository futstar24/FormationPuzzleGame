games = []
gameName = document.getElementById("gameName").innerHTML
link = "/sendGames/"+gameName
fetch(link).then(response => response.json()).then(function(data) {
    games = data["result"]
    createSearchResults(games)
})

function createSearchResults(games) {
    Array.from(gameResults.children).forEach(child => {
        child.parentElement.removeChild(child)
    })
    rowCount = 0
    itemNumber = 0
    gameRow = document.createElement("div")
    gameRow.classList.add("gameRow")
    gameRow.classList.add("selectorSearchRow")
    gameRow.classList.add("wrapper")
    games.forEach(game => {
        rowCount+=1
        if (rowCount > 5) {
            gameResults.appendChild(gameRow)
            gameRow = document.createElement("div")
            gameRow.classList.add("gameRow")
            gameRow.classList.add("selectorSearchRow")
            gameRow.classList.add("wrapper")
            rowCount = 0
        }
        gameItem = document.createElement("div")
        gameItem.classList.add("gameItem")
        gameItem.classList.add("wrapper")
        gameItem.classList.add("selectorSearchItem")
        gameItemText = document.createElement("p")
        gameItemText.classList.add("gameItemText")
        gameItemText.classList.add("selectorSearchItemText")
        gameItemText.id = game[8]
        gameDate = game[3].join("/")
        gameItemText.innerHTML = game[2]+"<br><br>"+game[0]+"<br>---<br>"+game[1]+"<br><br>"+gameDate
        gameItem.appendChild(gameItemText)
        gameRow.appendChild(gameItem)
        itemNumber+=1
    })
    gameResults.appendChild(gameRow)
    setupGameItems()
}

gameSearch.addEventListener("input",function() {
    matchingGames = []
    games.forEach(game => {
        if (game[1].toLowerCase().includes(gameSearch.value.toLowerCase())) {
            matchingGames.push(game)
        }
    })
    createSearchResults(matchingGames)
})

function setupGameItems() {
    Array.from(document.getElementsByClassName("gameItem")).forEach(gameItem => {
        gameItem.addEventListener("click", function() {
            gameId = gameItem.children.item(0).id
            selectGame.action = "/teamSelector/"+games[0][0]+"/"+gameId
            selectGame.submit()
        })
    })
}