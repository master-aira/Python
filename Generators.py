'''
Itarator - isme __next__() defined hota h
Iterable - isme __iter__ or __getitem__ defined hota hai
Iteration - process ko kehte hai
'''
# for i in range(11):
    # print(i)
def gen(n):
    for i in range(n):
        yield i
g = gen(10)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
h = "Harry" #Strings are Iterable
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())