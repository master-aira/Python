'''
i = 0
while True:
    if i < 5:
        i = i + 1
        continue
    print(i, end = " ")
    if i == 51:
        break
    i = i + 1
'''
#To make the user enter no. until he enter no.> 100
while True:
    n = int(input("No. Daalo Dada"))
    if n > 99:
        break