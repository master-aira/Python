class A:
    classvar1 = "I am in class A"
    def __init__(self):
        self.var1 = "I am class A's Constructor"
        self.classvar1 = "Instance variable in class A"
        self.special = "Special"
class B(A):
    classvar2 = "I am in class B"
    def __init__(self):
        # super().__init__()
        self.var1 = "I am class B's Constructor"
        self.classvar1 = "Instance variable in class B"
        super().__init__()
a = A()
b = B()
# print(b.classvar1)
print(b.special,b.var1,b.classvar1)