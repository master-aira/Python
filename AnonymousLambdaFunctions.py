#Lambda Functions or Anonymous Functions are One Liner Functions
def add(a,b):
    return a+b
add = lambda x,y:x+y
#Above two are same
def a_first(a):
    return a[0]
a = [[1,4] , [5,3] , [45,3]]
a.sort(key=a_first)
print(a)