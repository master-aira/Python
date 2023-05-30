class Employee:
    no_of_leaves = 10 #Sab ke hai ye Jaise ki yha pe Divya aur rohan Dono ke Liye hai Ye
    pass
Divya = Employee()
Rakesh = Employee()
Divya.name = "Divya"
Divya.salary = 100
Divya.role = "SDE"
Rakesh.name = "Rakesh"
Rakesh.Salary = 110
Rakesh.role = "Manager"
print(Divya.no_of_leaves)
print(Rakesh.no_of_leaves)
Employee.no_of_leaves = 15 #We can change it Aise Dono ka badal Jayega 
print(Divya.no_of_leaves)