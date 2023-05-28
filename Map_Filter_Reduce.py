n = ["59" , "4" , "34" , "10"]
# for i in range(len(n)):
#     n[i] = int(n[i])
n = list(map(int,n))
n[1] = n[1] + 1
print(n[1])
#def sq(x):
#    return x * x
a = [ 2,3,4,5,6,7,8]
print(list(map(lambda x : x * x,a)))
def sq(z):
    return z * z
def cube(z):
    return z * z * z
fun = [sq,cube]
for i in range(5):
    val = list(map(lambda c : c(i),fun))
    print(val)
f = [1,2,3,4,5,6,7,8,9]
def great5(num):
    return num > 5
gr = list(filter(great5,f)) #FILTER(kaise krna , kya kya krna h)
print(gr)
from functools import reduce
no = [1,2,3,4]
s = reduce(lambda g,h : g+h,no)
# s = 0
# for i in no:
#     s = s + i
print(s)