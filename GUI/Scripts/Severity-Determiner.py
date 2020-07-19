import math as M

class severity_details:
    def Pers_ques_and_optns(self):
        Pers_ques_and_optns = {
            "What is your gender?" : ["Male", "Female", "Other", "Rather not say"],
            "What is your age?" : 10
        }
        return Pers_ques_and_optns

    def Symp_ques_and_optns(self):
        Symp_ques_and_optns = {
            "What are your symptoms(if any)?" : ["Cough", "Fever", "Diarhhea", "Fatigue", "Headache", "Sore Throat", "Shortness of Breath", "Chest Pain", "Loss of Taste or Smell"],
            "Do you have any pre-existing conditions?" : ["Yes","No"],
            "What pre-existing condition do you have or have had?" : ["Any Heart condition", "All types of Cancer", "Diabetes", "Cystic Fibrosis", "AIDS or any other Immunodeficiency", "Epilepsy", ],
        }
        return Symp_ques_and_optns

    def Minor_ques_and_optns(self):
        Minor_ques_and_optns = {
            "How many times have you left your house in the past 2 weeks?" : 0,
            "Approximately how many separate people other than your family/room-mates have you come in close contact with?" : 0,
        }
        return Minor_ques_and_optns

    def Pers_answer_store(self,answers:list):
        self.Pers_answers = answers
    
    def Symp_answer_store(self,answers:list):
        self.Symp_answers = answers

    def Minor_answer_store(self,answers:list):
        self.Minor_answers = answers
    
    def weights(self):

        #initialization
        List_A = self.Pers_ques_and_optns()
        List_B = self.Symp_ques_and_optns()
        List_C = self.Minor_ques_and_optns()

        #weight determination
        List_A = list(List_A.values())
        List_B = list(List_B.values())
        List_C = list(List_C.values())
        print(List_A[0][0])
        print(List_A[1])

        List_A_optn_weights = {

            #weights of genders
            List_A[0][0] : 53/58,
            List_A[0][1] : 55/58,
            (str(List_A[0][2]), str(List_A[0][3])) : 1,
            
            #weights of age
            int(List_A[1]) : M.exp(List_A[1] / 43.42944) / 10
        }

        List_B_optn_weights = {                                          #allocating 3 points just to symptoms (subject to change)
            
            #weights of symptoms
            List_B[0][0] : 0.8,
            List_B[0][1] : 0.68,
            List_B[0][2] : 0.2,
            List_B[0][3] : 0.71, 
            List_B[0][4] : 0.35,
            List_B[0][5] : 0.39,
            List_B[0][6] : 1.15,
            List_B[0][7] : 1.09,
            List_B[0][8] : 0.34,

            #weights of pre-existing conditions
            List_B[2][0] : "Placeholder"
        }

        #tests
        print(List_A, end = "\n\n")
        print(List_B, end = "\n\n")
        print(List_C, end = "\n\n")
        print(List_A_optn_weights, end = "\n\n")
        print(List_B_optn_weights)

l = severity_details()
l.weights()