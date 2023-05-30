class Jee:
    no_of_students = "Bhut Saara"
    def __init__(self,sleep,main):
        self.neend = sleep
        self.jaruri = main
    def print_Details(self):
        return f"Main is {self.main}.Salary is {self.sleep}"
Subject = Jee(7,"Consistency")#Ye Argument hamesha init ko jaata hai
Requirements = Jee(7,"Study")
#Subject.main = "Physics and Chemistry"
#Requirements.sleep = 7
#Requirements.main = "Consistency"
#print(Requirements.print_Details())
print(Subject.neend)