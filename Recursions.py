# def print2(s):
#     print("This is",s)
# print2("Haa")
# n! - n * n-1 * n-2 * n-3 ... 1 eX - 5! = 5*4*3*2*1
'''
n = int(input("Kiska Factorial Chahiye"))
def Factorial(x): #Iterative
    u = 1
    for i in range(x):
        u = u * (i+1)
    return u    
print(Factorial(n))
'''
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# x = int(input("No. Daalo"))
# print(factorial(x))
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1)) + (fibonacci(n-2))
x = int(input("Number Daalo"))
print(fibonacci(x))