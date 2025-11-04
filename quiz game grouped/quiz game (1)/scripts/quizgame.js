let questionnumber = 0;
let score = 0;

const questions
{
    q:"What type is Golduck?",
    a:[
        {"1":"Water/Psychic",isCorrect : false},
        {"2":"Water",isCorrect : true},
        {"3":"Psychic",isCorrect : false},
        {"4":"Steel/Water",isCorrect : false}
    ]
},

function displayQuestion(){
    questioncontainer.innerHTML =`<h2>${questions[questionnumber].q}</h2>`
}