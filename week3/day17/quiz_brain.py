class QuizBrain:
    def __init__(self, q_list):
        self.q_list = q_list
        self.question_number = 0
        self.score = 0
    
    def next_question(self):
        question = self.q_list[self.question_number]
        prompt = question.question
        cur_answer = question.answer
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {prompt} (True/False)')
        self.check_answer(user_answer,cur_answer)

    def check_answer(self, user_answer, cur_answer):
        if user_answer.lower() == cur_answer.lower():
            self.score += 1
            print(f'Correct! Current score is {self.score}')
        else:
            print(f"I've never seen somebody more wrong than you. Score: {self.score}")
        print('\n')