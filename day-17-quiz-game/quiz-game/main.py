from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for q in question_data:
    question = Question(q["text"], q['answer'])
    question_bank.append(question)


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()