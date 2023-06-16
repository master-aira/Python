class A:
    def met(self):
        print("This is a method in class A")
class B(A):
    def met(self):
        print("This is a method in class B")
class C(A):
    def met(self):
        print("This is a method in class C")
class D(B,C):
    def met(self):
        print("This is a method in class D")
a = A()
b = B()
c = C()
d = D()
d.met()