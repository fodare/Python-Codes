from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain
"""Day 17 OOP
Concept, class and __init__() function"""

question_bank = []

for question in question_data:
    """ Loops through the question data and store
    the text and answers in the variable below"""
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz_brain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz! Please run the game again!")
print(f"Your final score is: {quiz.score} / {question_bank}")


