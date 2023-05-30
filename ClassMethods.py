class Jee:
    no_of_students = "Bhut Saara"
    def __init__(self,sleep,main):
        self.neend = sleep
        self.jaruri = main
    def print_Details(self):
        return f"Main is {self.main}.Salary is {self.sleep}"
    @classmethod
    def change_students_no(cls ,new_students_no):
        cls.no_of_students = new_students_no
Subject = Jee(7,"Consistency")#Ye Argument hamesha init ko jaata hai
Requirements = Jee(7,"Study")
#Subject.main = "Physics and Chemistry"
#Requirements.sleep = 7
#Requirements.main = "Consistency"
#print(Requirements.print_Details())
print(Subject.neend)
#Jee.no_of_students = "Badi Mani"
Subject.change_students_no("Badi Mani")
print(Subject.no_of_students)