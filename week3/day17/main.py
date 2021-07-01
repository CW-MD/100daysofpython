from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

more_questions = True

question_bank = []

for i in question_data:
    question_bank.append(Question(i['text'],i['answer']))

print()
new_quiz = QuizBrain(question_bank)

while new_quiz.question_number < len(question_bank):
    new_quiz.next_question()

