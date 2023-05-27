#Snake - Water - Gun
import random
choice = ["Snake" , "Water" , "Gun"]
n = 1
p = 0
cp = 0
while n <= 10 :
    a = random.choice(choice)    
    b = input("Enter Your Choice - Snake / Water / Gun ")
    if b == a:
        print(n)
        n = n + 1
    elif b == "Snake" and a == "Water":
        print("You Win")
        p = p + 1
        print("Point" , p)
        print(n)
        n = n + 1
    elif b == "Water" and a == "Gun":
        print("You Win")
        p = p + 1
        print("Point" , p)
        print(n)
        n = n + 1
    elif b == "Gun" and a == "Snake":
        print("You Win")
        p = p + 1
        print("Point" , p)
        print(n)
    else :
        cp = cp + 1
        print("You Lose" , cp)
        n = n + 1