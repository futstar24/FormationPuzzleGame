teams = []

fetch("/sendTeams").then(response => response.json()).then(function(data) {
    teams = data["teams"]
    teams.sort()
    createSearchResults(teams)
})

function createSearchResults(teams) {
    console.log(teamResults.children)
    Array.from(teamResults.children).forEach(child => {
        child.parentElement.removeChild(child)
    })
    rowCount = 0
    itemNumber = 0
    teamRow = document.createElement("div")
    teamRow.classList.add("teamRow")
    teamRow.classList.add("selectorSearchRow")
    teamRow.classList.add("wrapper")
    teams.forEach(team => {
        rowCount+=1
        if (rowCount > 5) {
            teamResults.appendChild(teamRow)
            teamRow = document.createElement("div")
            teamRow.classList.add("teamRow")
            teamRow.classList.add("selectorSearchRow")
            teamRow.classList.add("wrapper")
            rowCount = 0
        }
        teamItem = document.createElement("div")
        teamItem.classList.add("teamItem")
        teamItem.classList.add("selectorSearchItem")
        teamItem.classList.add("wrapper")
        teamItemText = document.createElement("p")
        teamItemText.classList.add("teamItemText")
        teamItemText.classList.add("selectorSearchItemText")
        teamItemText.id = "teamItemText"+itemNumber
        teamItemText.innerHTML = team
        teamItem.appendChild(teamItemText)
        teamRow.appendChild(teamItem)
        itemNumber+=1
    })
    teamResults.appendChild(teamRow)
    setupTeamItems()
}

teamSearch.addEventListener("input",function() {
    matchingTeams = []
    teams.forEach(team => {
        console.log(team)
        if (team.toLowerCase().includes(teamSearch.value.toLowerCase())) {
            console.log(team)
            matchingTeams.push(team)
        }
    })
    createSearchResults(matchingTeams)
})

function openTeamMenu(teamItem) {
    teamName = teamItem.children.item(0).innerHTML
    selectTeam.action = "/teamSelector/"+teamName
    selectTeam.submit()
}

function setupTeamItems() {
    Array.from(document.getElementsByClassName("teamItem")).forEach(teamItem => {
        teamItem.addEventListener("click", function() {
            openTeamMenu(teamItem)
        })
    })
}