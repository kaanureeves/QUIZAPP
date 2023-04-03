from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    questions_answer = question["correct_answer"]
    question_object = Questions(q_text=question_text, q_answer=questions_answer)
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

if(quiz.still_has_questions()==False):
    print("You have complete the quiz")
    print(f"Your final score is: {quiz.score}")