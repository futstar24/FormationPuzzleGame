fetch("/sendGameInfo").then(response => response.json()).then(function(data) {
    console.log(data)
    document.getElementById("gameName").innerHTML = data["tie"]
    startPuzzle(data)
})