from question_model import Question
from data import question_data
from quiz_model import Quiz

question_list = []

for ques in question_data:
    ques_text = ques['text']
    ques_ans = ques['answer']
    new_ques = Question(ques_text, ques_ans)
    question_list.append(new_ques)


quiz = Quiz(question_list)

print("#########################################################")
print("\nWelcome to MyQuiz\n")

while quiz.question_remaining():
    quiz.next_question()

print("#########################################################\n")
print(f"Your Score: {quiz.score} out of {2*len(quiz.ques_list)}")
print("Thank You!")
