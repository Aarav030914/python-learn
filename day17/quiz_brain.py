import html

import os
class QuizBrain:
    
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def ask_question(self):
        q_text = html.unescape(self.question_list[self.question_number].text)
        user_answer = input(f"Q {self.question_number + 1}: {q_text} (True/False)")
        os.system("clear") # for linux based systems
        
        if user_answer == self.question_list[self.question_number].ans:
            print("You are correct")
            self.score += 1
        else:
            print("You are wrong")
        print(f"The correct answer is {self.question_list[self.question_number].ans}")
        
        self.question_number += 1
                
    
    def still_has_questions(self):
        return self.question_number <= len(self.question_list)-1
            




                
        