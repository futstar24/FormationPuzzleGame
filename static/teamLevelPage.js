fetch("/sendGameInfo").then(response => response.json()).then(function(data) {
    console.log(data)
    startPuzzle(data)
})