import random


def quiz():
    correct_answers = 0
    incorrect_answers = 0
    quiz_questions = open("questions.txt", "r")
    quiz_questions_list = quiz_questions.readlines()
    random.shuffle(quiz_questions_list)
    for i in range(0, 5):
        question = quiz_questions_list[i].strip()
        question_answer = question.split(",")
        question_split = question_answer[0]
        answer_split = question_answer[1].lower()
        user_response = input(question_split + ' ').lower()
        if user_response == answer_split:
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect!")
            print("The correct answer is: " + answer_split.capitalize() + ".")
            incorrect_answers += 1
    score = 20 * correct_answers
    print("Quiz complete!  You answered " + str(correct_answers) + " correctly!")
    print("You scored " + str(score) + "%")


quiz()
