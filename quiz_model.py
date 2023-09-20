class Quiz:
    def __init__(self, ques_list):
        self.score = 0
        self.ques_num = 0
        self.ques_list = ques_list
        self.skipped_ques = []

    def next_question(self):
        current_question = self.ques_list[self.ques_num]
        self.ques_num += 1
        print(f"\nQ.{self.ques_num}: {current_question.text}? ")
        user_answer = input('Your answer: ')

        if user_answer.lower() == 'skip':
            print("Question Skipped!")
            self.skipped_ques.append(current_question)
        else: 
            self.check_answer(user_answer, current_question.answer)

    def check_answer(self, u_ans, c_ans):
        if u_ans.lower() == c_ans.lower():
            self.score += 2
            print("Correct!")
        else:
            self.score -= 1
            print("Wrong!")
        print()  

    def question_remaining(self):
        return self.ques_num < len(self.ques_list)

    def answer_skipped_questions(self):
        for skipped_question in self.skipped_ques:
            print(f"Skipped Question: {skipped_question.text}")
            user_input = input("Your answer: ")
            self.check_answer(user_input, skipped_question.answer)
        self.skipped_ques = []