def function1():
    print("Hello World")
fun = function1
del function1
fun() #Print Hoga Kyunki fun ek copy hai
def func(num):
    if num == 0:
        return print
    if num == 1:
        return sum
a = func(0)
print(a)
def ex(x):
    x("Hello")
ex(print)
def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexec
def who_is_harry():
    print("Harry is a good Boy")
who_is_harry = dec1(who_is_harry) #@dec1 bhi use kr skte hai is line ke badle def ke upar