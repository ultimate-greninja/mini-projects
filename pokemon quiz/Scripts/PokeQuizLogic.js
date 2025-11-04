function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
function checkCookiesInRange(range) {
    for (let i = 1; i <= 6; i++) {
        if (getCookie(`${range}${i}`) === "true") { // Ensure the cookie value is checked correctly
            return true;
        }
    }
    return false;
}
function questionCookies(){
    //this makes all the cookies for the question numbers
}
function QuestionsSelectionSetUp(){
    //rebuilds selection grid but without 
}
function QuestionSetUp(section,question){
    //this makes the question
    console.log(section,question)
}
//I suggest making a list of functions needed and think how i will do it

// question values

function questionValues(){
    // option 1
    let oneOne = ``
    let oneTwo = ``
    let oneThree = ``
    let oneFour = ``
    let oneFive = ``
    let oneSix = ``
    // option 2
    let twoOne = ``
    let twoTwo = ``
    let twoThree = ``
    let twoFour = ``
    let twoFive = ``
    let twoSix = ``
    // option 3
    let threeOne = ``
    let threeTwo = ``
    let threeThree = ``
    let threeFour = ``
    let threeFive = ``
    let threeSix = ``
    // option 4
    let fourOne = ``
    let fourTwo = ``
    let fourThree = ``
    let fourFour = ``
    let fourFive = ``
    let fourSix = ``
    // option 5
    let fiveOne = ``
    let fiveTwo = ``
    let fiveThree = ``
    let fiveFour = ``
    let fiveFive = ``
    let fiveSix = ``
    // option 6
    let sixOne = ``
    let sixTwo = ``
    let sixThree = ``
    let sixFour = ``
    let sixFive = ``
    let sixSix = ``
}

// question values

//cookies

if (!(
    checkCookiesInRange("one") ||
    checkCookiesInRange("two") ||
    checkCookiesInRange("three") ||
    checkCookiesInRange("four") ||
    checkCookiesInRange("five") ||
    checkCookiesInRange("six")
)) {
    console.log("Initializing cookies...");
    for (let i = 1; i <= 6; i++) {
        setCookie(`one${i}`, "true", 3);
        setCookie(`two${i}`, "true", 3);
        setCookie(`three${i}`, "true", 3);
        setCookie(`four${i}`, "true", 3);
        setCookie(`five${i}`, "true", 3);
        setCookie(`six${i}`, "true", 3);
    }
}

//cookies