# TODO: Asking the questions
# TODO: Checking if the answer was correct
# TODO: Checking if we're the end of the questions
from validationFunctions import inputValidation


class QuizBrain:

    def __init__(self,questionsList):
        """Initialize a new QuizBrain object."""
        self.question_number=0
        self.questions_list=questionsList
        self.score=0


    def validateAnswer(self,userAnswer,answer):
        """Validates the user answer."""

        if userAnswer == answer:
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong.")
            print(f"The correct answer was: {answer.capitalize()}")
            


    def stillHasQuestions(self):
        """"Verify if we still having questions in the question list. Returns True if there are and False otherwise"""
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False
        #return self.question_number < len(self.questions_list):  # Other form of solution.


    def nextQuestion(self):
        """"Show the current question and validates the user answer."""

        number=self.question_number+1
        question=self.questions_list[self.question_number].text
        answer=self.questions_list[self.question_number].answer.lower()

        userAnswer=inputValidation(f"Q.{number}: {question} (True/False): ",["True","False"]) # UserAnswer is in lower case
        self.question_number=number

        self.validateAnswer(userAnswer,answer)
