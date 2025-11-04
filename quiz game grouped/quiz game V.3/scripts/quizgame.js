let questionnumber = 0;
let score = 0;

const questions =
[
    {
        q:"1. What type is Golduck?",
        a:[
            {"1":"Water/Psychic",isCorrect:false},
            {"2":"Water",isCorrect:true},
            {"3":"Psychic",isCorrect:false},
            {"4":"Steel/Water",isCorrect:false},
        ]
    },
    {
        q:"2. What is Ditto's hidden ability?",
        a:[
            {"1":"Adaptabilty",isCorrect:false},
            {"2":"Limber",isCorrect:false},
            {"3":"Imposter",isCorrect:true},
            {"4":"Trace",isCorrect:false},        
        ]
    },
    {
        q:"3. What fossil does Kabuto come from?",
        a:[
            {"1":"Dome",isCorrect :true},
            {"2":"Old Amber",isCorrect:false},
            {"3":"Helix",isCorrect:false},
            {"4":"Sheild",isCorrect:false},
        ]
    },
    {
        q:"4. What region is Aipom from?",
        a:[
            {"1":"Kanto",isCorrect:false},
            {"2":"Hoenn",isCorrect:false},
            {"3":"Sinnoh",isCorrect:false},
            {"4":"Johto",isCorrect:true},
        ]
    },
    {
        q:"5. What is Unknown's ability?",
        a:[
            {"1":"Own Tempo",isCorrect:false},
            {"2":"Trace",isCorrect:false},
            {"3":"Levitate",isCorrect:true},
            {"4":"Magic Bounce",isCorrect:false},
        ]
    },
    {
        q:"6. What is Palkia's typing?",
        a:[
            {"1":"Water/Dragon",isCorrect:true},
            {"2":"Psychic/Dragon",isCorrect:false},
            {"3":"Water/Psychic",isCorrect:false},
            {"4":"Psychic",isCorrect:false},
        ]
    },
    {
        q:"7. Which one of these Pokemon dont have a Mega Evolution?",
        a:[
            {"1":"Groundon",isCorrect:true},
            {"2":"Gyrados",isCorrect:false},
            {"3":"Tyranitar",isCorrect:false},
            {"4":"Audino",isCorrect:false},
        ]
    },
    {
        q:"8. What type is Mudkip?",
        a:[
            {"1":"Ground",isCorrect:false},
            {"2":"Water/Ground",isCorrect:false},
            {"3":"Water",isCorrect:true},
            {"4":"Water/Electric",isCorrect:false},
        ]
    },
    {
        q:"9. What type is Azurill",
        a:[
            {"1":"Normal",isCorrect:false},
            {"2":"Water/Fairy",isCorrect:false},
            {"3":"Water",isCorrect:false},
            {"4":"Normal/Fairy",isCorrect:true},
        ]
    },
    {
        q:"10. What is Cacturne's hidden ability?",
        a:[
            {"1":"Water Absorb",isCorrect:true},
            {"2":"Sand Veil",isCorrect:false},
            {"3":"Sturdy",isCorrect:false},
            {"4":"Cclorophyll",isCorrect:false},
        ]
    },
    {
        q:"11. What is Altaria's typing?",
        a:[
            {"1":"Normal/Flying",isCorrect:false},
            {"2":"Dragon/Flying",isCorrect:true},
            {"3":"Fairy/Flying",isCorrect:false},
            {"4":"Flying",isCorrect:false},
        ]
    },
    {
        q:"12. How does Inkay evolve?",
        a:[
            {"1":"Level 30",isCorrect:false},
            {"2":"Level 20",isCorrect:false},
            {"3":"Level 30 and have the system upsidedown",isCorrect:true},
            {"4":"Level 20 and have the system upsidedown",isCorrect:false},
        ]
    },
    {
        q:"13. What is Mega Venasaur's ability?",
        a:[
            {"1":"Thick Fat",isCorrect:true},
            {"2":"Chlorophyll",isCorrect:false},
            {"3":"Overgrow",isCorrect:false},
            {"4":"Effect Spore",isCorrect:false},
        ]
    },
    {
        q:"14. What is Vigoroth's ability?",
        a:[
            {"1":"Traunt",isCorrect:false},
            {"2":"Thick Fat",isCorrect:false},
            {"3":"Vital Spirit",isCorrect:true},
            {"4":"Huge Power",isCorrect:false},
        ]
    },
    {
        q:"15. According to the Pokedex what happens when Spoink stop bouncing?",
        a:[
            {"1":"It gets stuck",isCorrect:false},
            {"2":"It spins",isCorrect:false},
            {"3":"its spring unravels",isCorrect:false},
            {"4":"its heart stops",isCorrect:true},
        ]
    },
    {
        q:"16. according to the Pokedex how long does the pain from houndooms flames stay?",
        a:[
            {"1":"A Month",isCorrect:false},
            {"2":"Forever",isCorrect:true},
            {"3":"A Year",isCorrect:false},
            {"4":"6 Months",isCorrect:false},
        ]
    },
    {
        q:"17. According to the Pokedex what does Cacturne do when it sees a traveler going through the dessert at night?",
        a:[
            {"1":"Follows them in a ragtag group waiting for them to tire",isCorrect:true},
            {"2":"attacks them",isCorrect:false},
            {"3":"guides them",isCorrect:false},
            {"4":"drags them through the sand",isCorrect:false},
        ]
    },
    {
        q:"18. According to the Pokedex Blissy can sense _______?",
        a:[
            {"1":"fear",isCorrect:false},
            {"2":"anger",isCorrect:false},
            {"3":"sadness",isCorrect:true},
            {"4":"happiness",isCorrect:false},
        ]
    },
    {
        q:"19. According to the Pokedex Phantump is?",
        a:[
            {"1":"Dead trees coming back to life",isCorrect:false},
            {"2":"Dead children who got lost in a forest",isCorrect:true},
            {"3":"Chopped trees coming back to life",isCorrect:false},
            {"4":"Dead Pokemon possesing a tree stump",isCorrect:false},
        ]
    },
    {
        q:"20. Jirachi's base stats are all _______?",
        a:[
            {"1":"63",isCorrect:false},
            {"2":"50",isCorrect:false},
            {"3":"77",isCorrect:false},
            {"4":"100",isCorrect:true},
        ]
    },
    {
        q:"21.How do you evolve Combee?",
        a:[
            {"1":"Level 21 and female",isCorrect:true},
            {"2":"Level 21 and male",isCorrect:false},
            {"3":"Level 21",isCorrect:false},
            {"4":"Level 21 and honey",isCorrect:false},
        ]
    },
    {
        q:"22. according to the pokedex what does drifloon dislike?",
        a:[
            {"1":"Trees",isCorrect:false},
            {"2":"Sharp objects",isCorrect:false},
            {"3":"Heavy children",isCorrect:true},
            {"4":"Ribbons",isCorrect:false},
        ]
    },
    {
        q:"23. How many spirits are in Spiritomb?",
        a:[
            {"1":"500",isCorrect:false},
            {"2":"666",isCorrect:false},
            {"3":"1",isCorrect:false},
            {"4":"108",isCorrect:true},
        ]
    },
    {
        q:"24. Why was Chatot banned from tournaments?",
        a:[
            {"1":"High stats",isCorrect:false},
            {"2":"Too loud",isCorrect:false},
            {"3":"A move used custom audio",isCorrect:true},
            {"4":"A glitch made it invincible",isCorrect:false},
        ]
    }
];
function displayQuestion(){
    questioncontainer.innerHTML =`<h2>${questions[questionnumber].q}</h2>`
}
choice(num)
{
    if (num == 1) {
        console.log(1)
    } else if (num == 2) {
        console.log(2)
    } else if (num == 3) {
        console.log(3)
    } else {
        console.log(4)
    }
}
