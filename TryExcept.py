n1 = input("Koi No. Daalo")
n2 = input("Yha bhi")
try:
    print("Sum =",int(n1)+int(n2))
except Exception as a: #Exception ko a mein store kr leta h
    print(a)
print("Yhi Tha")