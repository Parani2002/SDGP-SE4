// Quiz data
const questions = [
  {
    question: "Question 1: What is 2 + 2?",
    answers: ["3", "4", "5", "6"],
    correctAnswer: "4",
  },
  {
    question: "Question 2: What is the capital of France?",
    answers: ["London", "Berlin", "Paris", "Madrid"],
    correctAnswer: "Paris",
  },
];

let currentQuestionIndex = 0;
let userScore = 0;

// Function to start the quiz based on qualification
function startQuiz(qualification) {
  document.getElementById("qualification-buttons").style.display = "none";
  displayQuestion();
}

// Function to display quiz question
function displayQuestion() {
  const quizContainer = document.getElementById("quiz-container");
  const currentQuestion = questions[currentQuestionIndex];

  quizContainer.innerHTML = `
      <h2>${currentQuestion.question}</h2>
      <div id="answers">
        ${currentQuestion.answers
          .map(
            (answer) => `
          <button class="button1" onclick="checkAnswer('${answer}')">${answer}</button>`,
          )
          .join("")}
      </div>
      <p class="center-paragraph">Question ${currentQuestionIndex + 1} of ${questions.length}</p>
    `;
}

// Function to check the selected answer
function checkAnswer(answer) {
  const currentQuestion = questions[currentQuestionIndex];
  if (answer === currentQuestion.correctAnswer) {
    userScore++;
  }
  currentQuestionIndex++;
  if (currentQuestionIndex < questions.length) {
    displayQuestion();
  } else {
    showResult();
  }
}

// Function to display quiz result
function showResult() {
  const quizContainer = document.getElementById("quiz-container");
  quizContainer.innerHTML = `
      <h2>Quiz Completed!</h2>
      <br>
      <p class="center-paragraph">Your score: ${userScore} out of ${questions.length}</p>
    `;
}
