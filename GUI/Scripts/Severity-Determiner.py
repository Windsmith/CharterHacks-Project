import math as M

class Process:
    def get_set_1(self):
        multi = ""
        Pers_ques_and_optns = {
            "What is your gender?" : [{multi : False}, ["Male", "Female", "Other", "Rather not say"]],
            "What is your age?" : [{multi : False}, 10]
        }
        return Pers_ques_and_optns

    def get_set_2(self):
        multi = ""
        Symp_ques_and_optns = {
            "What are your symptoms(if any)?" : [{multi : True}, ["Cough", "Fever", "Diarhhea", "Fatigue", "Headache", "Sore Throat", "Shortness of Breath", "Chest Pain", "Loss of Taste or Smell"]],
            "Do you have any pre-existing conditions?" : [{multi : False}, ["Yes","No"]],
            "What pre-existing condition do you have or have had?" : [{multi : True}, ["Any Heart condition", "All types of Cancer", "Obesity", "Cystic Fibrosis", "AIDS or any other Immunodeficiency", "Diabetes", "Asthma", "Hypertension", "Liver Disease"]],
        }
        return Symp_ques_and_optns

    def get_set_3(self):
        multi = ""
        Minor_ques_and_optns = {
            "How many times have you left your house in the past 2 weeks?" : [{multi : False}, 2],
            "Approximately how many separate people other than your family/room-mates have you come in close contact with?" : [{multi : False}, 20],
        }
        return Minor_ques_and_optns

    def result_1(self,answers:list):
        self.Pers_answers = answers
    
    def result_2(self,answers:list):
        self.Symp_answers = answers

    def result_3(self,answers:list):
        self.Minor_answers = answers
    
    def weights(self):

        #initialization
        List_A = self.get_set_1()
        List_B = self.get_set_2()
        List_C = self.get_set_3()

        #weight determination
        List_A = list(List_A.values())
        List_B = list(List_B.values())
        List_C = list(List_C.values())
        print(List_A[0][1][0])
        print(List_A[1][1])

        List_A_optn_weights = {

            #weights of genders
            List_A[0][1][0] : 53/58,
            List_A[0][1][1] : 55/58,
            (List_A[0][1][2], List_A[0][1][3]) : 1,
            
            #weight of age
            int(List_A[1][1]) : M.exp(List_A[1][1] / 43.42944) / 10
        }

        List_B_optn_weights = {                                          #allocating 3 points just to symptoms (subject to change)
            
            #weights of symptoms
            List_B[0][1][0] : 0.8,
            List_B[0][1][1] : 0.68,
            List_B[0][1][2] : 0.2,
            List_B[0][1][3] : 0.71, 
            List_B[0][1][4] : 0.35,
            List_B[0][1][5] : 0.39,
            List_B[0][1][6] : 1.15,
            List_B[0][1][7] : 1.09,
            List_B[0][1][8] : 0.34,

            #weights of pre-existing conditions
            List_B[2][1][0] : 0.97,
            List_B[2][1][1] : 1.02,
            List_B[2][1][2] : 0.89,
            List_B[2][1][3] : 1.1,
            List_B[2][1][4] : 0.87,
            List_B[2][1][5] : 0.86,
            List_B[2][1][6] : 0.62,
            List_B[2][1][7] : 0.57,
            List_B[2][1][8] : 0.59
        }

        List_C_optn_weights = {
            List_C[0][1] : List_C[0][1] / 10,
            List_C[1][1] : List_C[1][1] / 25
        }

        #tests
        print(List_A, end = "\n\n")
        print(List_B, end = "\n\n")
        print(List_C, end = "\n\n")
        print(List_A_optn_weights, end = "\n\n")
        print(List_B_optn_weights, end = "\n\n")
        print(List_C_optn_weights)

l = Process()
l.weights()
