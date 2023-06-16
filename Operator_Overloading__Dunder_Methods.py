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
    def __add__(self,other):
        return self.neend + other.neend
    def __truediv__(self,other):
        return self.neend / other.neend
    def __repr__(self):
        return f"Sleep ({self.neend},'{self.jaruri}') "
    def __str__(self):
        return f"Main is {self.neend} & Salary is {self.jaruri}"
jee1 = Jee(5,"Haan")
jee2 = Jee(65,"Haannn")
print(jee1 + jee2)
print(jee1 / jee2)
print(jee1)