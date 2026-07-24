from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def createQuestionBank(questionsData):
    """Create a bank of questions. Returns a list of Question objects"""
    listQuestions=[]
    for data in questionsData:
        text=data["question"]
        answer=data["correct_answer"]
        q1=Question(text,answer)
        listQuestions.append(q1)

    return listQuestions

questionBank=createQuestionBank(question_data)

quiz=QuizBrain(questionBank)


#for i in range(10):

while quiz.stillHasQuestions():
    quiz.nextQuestion()
    print(f"Your current score is: {quiz.score}/{quiz.question_number}")
    print("\n")

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
