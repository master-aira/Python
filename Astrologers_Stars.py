n = int(input("Kitna"))
b = int(input("0 for Ulta & 1 for Seedha"))
c = bool(b)
print(c)
i = 1
while c == True:
    print("*" * i)
    i = i + 1
    if i > n:
        break
while c == False:
    print("*" * n)
    n = n - 1
    if i > n:
        break