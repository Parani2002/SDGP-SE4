const questions = [
  {
    question: "Question 1: Skill 1",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 2",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 3",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 4",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 5",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 6",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 7",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 8",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 9",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 10",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 11",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 12",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 13",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 14",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 15",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 16",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 17",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 18",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 19",
    answers: ["1", "2", "3", "4"],
  },
  {
    question: "Question 2: Skill 20",
    answers: ["1", "2", "3", "4"],
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
  const quizContainer = document.getElementById("container-container");
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
  const quizContainer = document.getElementById("container-container");
  quizContainer.innerHTML = `
      <h2>Quiz Completed!</h2>
      <br>
      <p class="center-paragraph">Your score: ${userScore} out of ${questions.length}</p>
    `;
}
