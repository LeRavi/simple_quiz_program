class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right, well done my dear!🙋 ")
        else:
            print(f"Not quite the answer I was looking for 😥")
            print(f"The right answer is {correct_ans}")
        print(f"Your current score is: {self.score} / {self.question_number}")
        print("\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: {current_question.text} (True or False ?): ")
        self.check_answer(user_answer, current_question.answer)








