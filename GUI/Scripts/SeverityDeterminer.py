'''
=================================================================================================================================================

                                                  Tutorial on the usage of the class

=================================================================================================================================================

1) The methods under the Getter Methods are for getting either the question and option sets or the severity.
   The get_set_<number>() methods returns a set of the questions in the form of a dictionary, key is the question and the values are the options
   The get_severity() method returns the final severity of situation when called (Shri can make final verdict from it.)

2) The methods under the Input Methods are for inputting the values (That Anand gets from user)
   The result_<number>() method takes the input list as an arg, for each set of questions

 # This shouldn't be interacted with #

3) The method under the Weight Storage is for Weight Storage (obviously)

PLEASE NOTE:= The order to use the methods should be input first, then get the severity
              Also the options with number inputs will not have a value unless an input is made
'''

import math as M

class Process:

    # Getter Methods
    def get_set_1(self):
        Pers_ques_and_optns = {
            "What is your gender?" : [{"multi" : False}, ["Male", "Female", "Other", "Rather not say"]],
            "What is your age?" : [{"multi" : None}, []]
        }
        return Pers_ques_and_optns

    def get_set_2(self):
        Symp_ques_and_optns = {
            "What are your symptoms(if any)?" : [{"multi" : True}, ["Cough", "Fever", "Diarhhea", "Fatigue", "Headache", "Sore Throat", "Shortness of Breath", "Chest Pain", "Loss of Taste or Smell"]],
            "Do you have any pre-existing conditions?\n If yes, what pre-existing condition do you have or have had?" : [{"multi" : True}, ["Any Heart condition", "All types of Cancer", "Obesity", "Cystic Fibrosis", "AIDS or any other Immunodeficiency", "Diabetes", "Asthma", "Hypertension", "Liver Disease", "No pre-existing conditions"]],
        }
        return Symp_ques_and_optns

    def get_set_3(self):
        Minor_ques_and_optns = {
            "How many times have you left your house in the past 2 weeks?" : [{"multi" : None}, []],
            "Approximately how many separate people other than\n your family/room-mates have you come in close contact with?" : [{"multi" : None}, []],
        }
        return Minor_ques_and_optns

    # Input Methods
    def result_1(self,answers:list):
        self.Pers_answers = answers
    
    def result_2(self,answers:list):
        self.Symp_answers = answers

    def result_3(self,answers:list):
        self.Minor_answers = answers

    # Weight storage (Not to be interacted with)
    def weights(self):

        # Initialization
        List_A = self.get_set_1()
        List_B = self.get_set_2()
        List_C = self.get_set_3()

        # Weight determination
        List_A = list(List_A.values())
        List_B = list(List_B.values())
        List_C = list(List_C.values())

        self.List_A_optn_weights = {

            # Weights of genders
            List_A[0][1][0] : 53/58,
            List_A[0][1][1] : 55/58,
            (List_A[0][1][2], List_A[0][1][3]) : 1,
            
            # Weight of age
            self.Pers_answers[1] : M.exp(self.Pers_answers[1] / 43.42944) / 10
        }

        self.List_B_optn_weights = {                                          # Allocating 3 points just to symptoms (subject to change)
            
            # Weights of symptoms
            List_B[0][1][0] : 0.8,
            List_B[0][1][1] : 0.68,
            List_B[0][1][2] : 0.2,
            List_B[0][1][3] : 0.71, 
            List_B[0][1][4] : 0.35,
            List_B[0][1][5] : 0.39,
            List_B[0][1][6] : 1.15,
            List_B[0][1][7] : 1.09,
            List_B[0][1][8] : 0.34,

            # Weights of pre-existing conditions
            List_B[1][1][0] : 0.97,
            List_B[1][1][1] : 1.02,
            List_B[1][1][2] : 0.93,
            List_B[1][1][3] : 1.1,
            List_B[1][1][4] : 0.95,
            List_B[1][1][5] : 0.9,
            List_B[1][1][6] : 0.62,
            List_B[1][1][7] : 0.57,
            List_B[1][1][8] : 0.59
        }

        self.List_C_optn_weights = {
            self.Minor_answers[0] : self.Minor_answers[0] / 10,
            self.Minor_answers[1] : self.Minor_answers[1] / 25
        }

    def get_severity(self):

        self.weights()
        severity_counter = 0
        
        for element in self.Pers_answers:
            severity_counter += self.List_A_optn_weights[element]
        
        for element in self.Symp_answers:
            if type(element) == list:
                for option in element:
                    severity_counter += self.List_B_optn_weights[option]
        
        for element in self.Minor_answers:
            severity_counter += self.List_C_optn_weights[element]

        if severity_counter > 10:
            severity_counter = 10

        return severity_counter

# Example Test

l = Process()
l.result_1(["Female", 50])
l.result_2([["Cough", "Fever", "Fatigue", "Shortness of Breath"], "Yes", ["Cystic Fibrosis", "Hypertension"]])
l.result_3([5,25])
