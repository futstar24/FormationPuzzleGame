dailyPlayerList = localStorage.getItem("dailyPlayerList")

if (dailyPlayerList != "" && dailyPlayerList != null) {
    dailyPlayerList = dailyPlayerList.split(",")
} else {
    localStorage.setItem("dailyPlayerList","")
    dailyPlayerList = localStorage.getItem("dailyPlayerList")
}

setDailyPlayerList(dailyPlayerList)

fetchDailyFormation()
resetAtMidnight()
//resetDaily()

function resetAtMidnight() {
    var now = new Date();
    night = new Date(); 
    night.setDate(new Date().getDate()+1)
    night.setHours(0)
    night.setMinutes(0)
    night.setSeconds(5)
    night.setMilliseconds(0)
    msToMidnight = night.getTime() - now.getTime();
    setTimeout(function() {
      resetDaily();
      resetAtMidnight();
    }, msToMidnight);
};

function resetDaily() {
    console.log("reloading")
    localStorage.setItem("dailyPlayerList","")
    location.reload()
}

function fetchDailyFormation() {
    fetch("/dailyFormation").then(response => response.json()).then(function(data) {
        formationData = data
        console.log(formationData["randomNumber"])
        document.getElementById("gameName").innerHTML = formationData["tie"]
        startPuzzle(formationData)
    })
}

teamsButton.addEventListener("click", function() {
    teamSelectorForm.submit()
})