L = 10 # Global Yani ki Khi bhi ja skta h function ke andar bhar khi bhi 
# Jab Local mein nhi milega toh Global mein check kiya Jayega
def f1(n):
    m = 5 #Local Yani bas andar hi rahega
    global L #Aise AB global variable ko change kr skte hai
    L = L + 10
    print(L,m,n,"Those are great")
f1("He is good but")
#Global wla bas Global mein hi Dekhega
def Harry():
    x = 10
    def Laura(): #Nested Function
        global x #ye seedha bhar jayega aur x nhi milne par new x bna dega [Local mein nhi jayega]
        x = 20
    print(x)
    Laura()
    print(x) #Call ke baad bhi x = 10 darshata hai ki Local x nhi badla
Harry()
print(x) #New x hai ye jo Laura ne banaya hai