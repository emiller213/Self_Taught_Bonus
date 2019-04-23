import random


def quiz():
    correct_answers = 0
    with open("questions.txt") as file:
        quiz_questions_list = file.readlines()
        random.shuffle(quiz_questions_list)
    for i in range(0, 5):
        question_answer = quiz_questions_list[i].strip().split(",")
        user_response = input(question_answer[0] + ' ').lower()
        if user_response == question_answer[1].lower():
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect!")
            print("The correct answer is: " + question_answer[1].capitalize() + '.')
    print("Quiz complete!  You answered " + str(correct_answers) + " correctly!")
    print("You scored " + str(correct_answers * 20) + "%")


quiz()
