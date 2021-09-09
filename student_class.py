import random
from tkinter import *
class Student:
    
    def __init__(self, player_n, player_l, player_a):
        self.player_name = player_n
        self.player_lvl = player_l
        self.player_age = player_a
        
    def name_verification(self):
        if len(self.player_name)==0:
            return "✘ Must Enter A Name"
            
       
        else:
            return "Valid                             "
    
    #def age_verification2(self):
      #  if self.player_age >11:
      #      return "✘ Must be 5-11"
     #   else:
      #     return "Valid"
#
    def age_verification(self):
        try: 
            int(self.player_age)
            return "Valid       "
        except ValueError:
            return "✘ Must Enter A Number"

    def level_verification(self):
        if self.player_lvl == "Select Level":
            return "✘ Level Required"
        else:
            return "Valid       "
    def check_answer(self,var1, count):
        if len(var1.get())==0:
            self.feedback_empty()
        else:
            if var1.get() == str(self.correct_answer()):
                self.score +=1
                self.feedback_correct()
                self.check.grid_remove()
                self.next_button_create()
            else:
                self.feedback_wrong()
                self.check.grid_remove()
                self.next_button_create()
                 
                 # If the count == 11 times 
                
            
    def write_file(self):
        results_file = open("math_results.text", "a")
        results_file.write("-------------------------\n")
        results_file.write(f"Student Name: {self.student_name} \n"
                            f"Year Level: {self.range} \n"
                            f"Operation: {self.difficulty}\n")
        
        results_file.write("-------------------------\n")
        results_file.close()
        
    
        
        