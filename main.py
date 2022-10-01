from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from data import personal_data
question_bank = []


for q_and_ans in personal_data:
    question_text = q_and_ans["question"]
    question_answer = q_and_ans["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz\nYour final score is {quiz.score} / {quiz.question_number}")


