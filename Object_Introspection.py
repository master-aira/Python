class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname},{lname}@codewithharry.com"
    def explain(self):
        return f"This Employee is ({self.fname},{self.lname})"
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "E-mail Not found"
        return f"{self.fname},{self.lname}@codewithharry.com"
    @email.setter
    def email(self,string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
hindustani_supporter =Employee("Hindustani","Supporter")
nikhil_raj_pandey =Employee("Nikhil_Raj","Pandey")
print(hindustani_supporter.explain())
print(hindustani_supporter.email)
hindustani_supporter.fname = "US"
print(hindustani_supporter.email)
hindustani_supporter.email = "this.that@codewithharry.com"
print(hindustani_supporter.email)
del hindustani_supporter.email
print(hindustani_supporter.email)
skillf = Employee("Skill","F")
print(skillf.email)
print(type("It's a String"))
print(id("It's a String"))
print(dir("It's a String"))
import inspect
print(inspect.getmembers(skillf))