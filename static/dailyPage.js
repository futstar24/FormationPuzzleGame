//famousFormations


searchMenu = document.getElementById("searchMenuWrapper")
setupSearchMenu()
searchMenu.parentElement.removeChild(searchMenu)
submitButton = document.getElementById("submitButton")
setupSubmitButton()
submitButton.parentElement.removeChild(submitButton)
players = null
formation = null
lastRow = null
formationData = null

formationData = null
fetch("/dailyFormation").then(response => response.json()).then(function(data) {
    formationData = data
    startPuzzle(formationData)
})

document.body.addEventListener("click", function(evt) {
    if (!searchMenu.contains(evt.target) && !evt.target.classList.contains("formationPosition") && !evt.target.classList.contains("positionText") && document.body.contains(searchMenu)) {
        searchMenu.parentElement.removeChild(searchMenu)
    }
})

function startPuzzle(formationData) {

    formation = formationData["formation"]
    formation.reverse()
    formation.push(1)

    players = formationData["lineup"]
    positionNumber = 0

    for (var i = 0; i < formation.length; i++) {
        isLastRow = false
        if (i == formation.length-1) {
            isLastRow = true
        }
        positionNumber = createFormationRow(formation[i],isLastRow,positionNumber)
    }
}

function createFormationRow(numItems,isLastRow,positionNumber) {
    row = document.createElement("div")
    row.classList.add("formationRow")
    spaceBetweenRows = 10
    if (formation.length == 5) {
        spaceBetweenRows = 6
    } else if (formation.length == 6) {
        spaceBetweenRows = 4
    }
    totalEmptySpace = spaceBetweenRows*(formation.length-1)
    rowHeight = (100-totalEmptySpace)/formation.length
    row.style.height = rowHeight+"%"
    if (numItems == 2) {
        row.style.gap = "7vh"
    } else if (numItems == 3 || numItems == 4) {
        row.style.gap = "6vh"
    }
    for (var i = 0; i < numItems; i++) {
        position = document.createElement("div")
        position.classList.add("formationPosition")
        position.classList.add("wrapper")
        text = document.createElement("p")
        text.classList.add("positionText")
        text.id = "position"+positionNumber
        positionNumber+=1
        position.appendChild(text)
        row.appendChild(position)
    }
    formationSetup.appendChild(row)
    if (!isLastRow) {
        spacer = document.createElement("div")
        spacer.style.height = spaceBetweenRows+"%"
        formationSetup.appendChild(spacer)
    } else {
        lastRow = row
    }
    setupPositions()
    return positionNumber
}

selectedPosition = null

function setupPositions() {
    Array.from(document.getElementsByClassName("formationPosition")).forEach(position => {
        addPositionClick(position)
    })
}

function addPositionClick(position) {
    position.addEventListener("click", function() {
        selectedPosition = position
        document.body.appendChild(searchMenu)
        searchPlayers.focus()
        searchPlayers.value = ""
        searchPlayers.addEventListener("input", resetAndReload)
        reloadResults()
    })
}

function resetAndReload() {
    resetResults()
    reloadResults()
}

function reloadResults() {
    filledSpots = 0
    //change to be full player list, from api?
    players.toSorted().every(player => {
        if (player.toLowerCase().includes(searchPlayers.value.toLowerCase())) {
            console.log(player)
            document.getElementById("player"+filledSpots).innerHTML = player
            filledSpots += 1
        }
        if (filledSpots == 10) {
            return false
        } else if (filledSpots == 0) {
            document.getElementById("player0").innerHTML = "No players found."
        }
        return true
    })
}

function resetResults() {
    for (var i = 0; i < 10; i++) {
        document.getElementById("player"+i).innerHTML = ""
    }
}

function checkIfSubmittable() {
    counter = 0
    Array.from(document.getElementsByClassName("positionText")).forEach(playerName => {
        if (playerName.innerHTML != "") {
            counter+=1
        }
    })
    if (counter == 11) {

        lastRow.appendChild(submitButton)
    }
}

function setupSearchMenu() {
    Array.from(document.getElementsByClassName("playerSearchResult")).forEach(searchResult => {
        searchResult.addEventListener("click", function() {
            player = searchResult.children.item(0).innerHTML
            if (player != "" && player != "No players found.") {
                selectedPlayer = searchResult.children.item(0).innerHTML
                selectedPosition.children.item(0).innerHTML = selectedPlayer
                checkIfSubmittable()
                searchMenu.parentElement.removeChild(searchMenu)
            }
        })
    })
}

function setupSubmitButton() {
    submitButton.addEventListener("click", function() {
        correctPlayers = 0
        for (var i = 0; i < 11; i++) {
            if (document.getElementById("position"+i).innerHTML == formationData["lineup"][i]) {
                correctPlayers += 1
            }
        }
        if (correctPlayers == 11) {
            alert("You win!")
        } else {
            alert("You lose!")
        }
    })
}
