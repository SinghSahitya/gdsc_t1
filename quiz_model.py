class Quiz:
    def __init__(self, ques_list):
        self.score = 0
        self.ques_num = 0
        self.ques_list = ques_list

    def next_question(self):
        current_question = self.ques_list[self.ques_num]
        self.ques_num += 1
        print(f"Q.{self.ques_num}: {current_question.text}? ")
        user_answer = input('Your answer: ')
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, u_ans, c_ans):
        if u_ans.lower() == c_ans.lower():
            self.score += 2
            print("Correct!!")
        else:
            self.score -= 1
            print("Wrong!!")
        print()  

    def question_remaining(self):
        return self.ques_num < len(self.ques_list)
