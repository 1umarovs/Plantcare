const quizData = [
    {
        question: "1. O'simlik uchun qancha vaqt ajratasiz?",
        a: "30 daqiqadan kamroq",
        b: "30 daqiqa atrofida",
        c: " 1 soat va undan ko'proq",
    },
    {
        question: "2. O'simlik o'sadigan muhitda uy hayvoni ham mavjudmi?",
        a: "ha, kuchuk boqaman",
        b: "ha, mushuk boqaman",
        c: "yoq",
    },
    {
        question: "3. O'simlik parvarishlash bo'yicha malakangiz qanday?",
        a: "expert",
        b: "qiziqaman, malumotlar qidirib parvarishlayman",
        c: "boshlang'ich",
    },
    {
        question: "4. O'simlik parvarish qilmoqchi bo'lgan muhitda yoruqlik qay darajada?",
        a: "yuqori",
        b: "o'rta",
        c: "past",
    },
    {
        question: "5. Qanday hajmdagi o'simliklarni parvarishlashni yoqtirasiz?",
        a: "katta",
        b: "o'rta",
        c: "kichik",
    },
];
const quiz= document.getElementById('quiz')
const answerEls = document.querySelectorAll('.answer')
const questionEl = document.getElementById('question')
const a_text = document.getElementById('a_text')
const b_text = document.getElementById('b_text')
const c_text = document.getElementById('c_text')
const submitBtn = document.getElementById('submit')
let currentQuiz = 0
let score = 0
loadQuiz()
function loadQuiz() {
    deselectAnswers()
    const currentQuizData = quizData[currentQuiz]
    questionEl.innerText = currentQuizData.question
    a_text.innerText = currentQuizData.a
    b_text.innerText = currentQuizData.b
    c_text.innerText = currentQuizData.c
}
function deselectAnswers() {
    answerEls.forEach(answerEl => answerEl.checked = false)
}
function getSelected() {
    let answer
    answerEls.forEach(answerEl => {
        if(answerEl.checked) {
            answer = answerEl.id
        }
    })
    return answer
}
let a = 0
let b = 0
let c = 0

submitBtn.addEventListener('click', () => {
    const answer = getSelected()
    console.log(answer==='a');
    console.log(answer==b);
    console.log(answer==='c');

    if(answer) {
       if(answer === 'a') {
        a++
       }
       if(answer === 'b') {
        b++
       }
       if(answer === 'c') {
        c++
       }

       currentQuiz++
       if(currentQuiz < quizData.length) {
           loadQuiz()
       } else {
        if (a > b && a > c){
            quiz.innerHTML = `
            <h2>Siz hovli o'simliklariga qiziqasiz</h2>
            <a class="btn btn-success" href="/plants">o'simliklar</a><br><br>`
        }
        else if(b > a && b > c){
            quiz.innerHTML = `
            <h2>Siz  gulli  o’simlik yoki katta o’simliklarga qiziqasiz</h2>
            <a class="btn btn-success" href="/plants">o'simliklar</a><br><br>`
                }
        else if(c > a && b < c){
            quiz.innerHTML = `
            <h2>Siz noyob o’simliklar qiziqasiz</h2>
            <a class="btn btn-success" href="/plants">o'simliklar</a><br><br>`
            
        }
        else if(c == b && c >a){
            quiz.innerHTML = `
            <h2>Siz noyob o’simliklar va gulli  o’simlik yoki katta o’simliklarga qiziqasiz</h2>
            <a class="btn btn-success" href="/plants">o'simliklar</a><br><br>`
        }
        else if(c == a && c >b){
            quiz.innerHTML = `
            <h2>Siz noyob o’simliklar va hovli o'simliklariga  qiziqasiz</h2>
            <a class="btn btn-success" href="/plants">o'simliklar</a><br><br>`
            
        }

        else if(b == a && c <b){
            quiz.innerHTML = `
            <h2>Siz gulli  o’simlik,katta o’simliklarga va hovli o'simliklariga  qiziqasiz</h2>
            <a class="btn btn-success" href="/plants">o'simliklar</a><br><br>`

        }

    }
       }
    }
)
