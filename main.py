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
print("Instructions:\n1. Answer either 'True' or 'False'.\n2. You can skip the questions by typing 'skip'.\n3. Skipped questions can be attempted at the end of the quiz.")
print("")

while quiz.question_remaining():
    quiz.next_question()

if quiz.skipped_ques:
    user_choice = input("\nYou have skipped questions. Would you like to attempt them? (yes/no): ")
    if user_choice.lower() == 'yes':
        quiz.answer_skipped_questions()

print("#########################################################\n")
print(f"Your Score: {quiz.score} out of {2*len(quiz.ques_list)}")
print("Thank You!")


